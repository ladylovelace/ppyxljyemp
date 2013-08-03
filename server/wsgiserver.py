#!/usr/bin/python
from gevent.pywsgi import WSGIServer
import urllib

port = 1234 # TODO change later to best port

def search(cnpj):
    apiKey = 'ec3abef2e4a45853b1e2d2aa121b0106'
    url = 'http://irql.bipbop.com.br/?q=SELECT FROM \'RFB\'.\'CERTIDAO\' WHERE \'DOCUMENTO\' = \'' + cnpj + '\'&apiKey=' + apiKey 
    
    a = urllib.urlopen(url).read()
    return a

def application(env, start_response):
    if env['PATH_INFO'] == '/':
        q = env['QUERY_STRING'].split("q=")
        
        try:
            print q[1]
            cnpj = q[1]
            
            #validate (cnpj)
            # if cnpj is only numbers you can search
            # TODO change for real query
            response = search(cnpj)
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [response]
        except IndexError:      
            start_response('200 OK', [('Content-Type', 'text/html')])
            return ["<b>boo</b>"]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return ['<h1>Not Found :(</h1>']

def main():
    server = WSGIServer(('', port), application)
    try:
        print("Fishes on %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print(' now sleeping with the fishes')
        server.stop()

if __name__ == '__main__':
    main()

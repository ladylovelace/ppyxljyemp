import http.server
import socketserver
import urllib.parse

class httpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.log_message("%s %s" % (self.command, self.path) )
        self.dumpReq( None )

    def do_POST(self):
        self.log_message("%s %s" % (self.command, self.path) )
        if self.headers.has_key('content-length'):
            length= int( self.headers['content-length'] )
            self.dumpReq( self.rfile.read( length ) )
        else:
            self.dumpReq( None )

    def dumpReq( self, formInput=None ):   
        response= "<html><head></head><body>"
        response+= "<p>boo</p>"
        response+= "<p>HTTP Request</p>"
        response+= "<p>self.command= <tt>%s</tt></p>" % ( self.command )
        response+= "<p>self.path= <tt>%s</tt></p>" % ( self.path )
        response+= "</body></html>"
        self.sendPage( "text/html", response )

    def sendPage( self, type, body ):
        self.send_response( 200 )
        self.send_header( "Content-type", type )
        self.send_header( "Content-length", str(len(body)) )
        self.end_headers()
        self.wfile.write( bytes(body, 'UTF-8') )

def main():
    try:
        server = socketserver.TCPServer(("", 80), httpHandler)
        print ("AWWW YEAHHH!1")
        server.serve_forever()
    except KeyboardInterrupt:
        print ("WHY?! Service killed by keyboard :(")
        server.socket.close()
        print ("dead.")

if __name__ == '__main__':
    main(); 
    
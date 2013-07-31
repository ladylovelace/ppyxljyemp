import http.server
import socketserver

def main():
    try:
        server = socketserver.TCPServer(("", 12000), http.server.SimpleHTTPRequestHandler)
        print ("AWWW YEAHHH!1")
        server.serve_forever()
    except KeyboardInterrupt:
        print ("WHY?! Service killed by keyboard :(")
        server.socket.close()
        print ("dead.")

if __name__ == '__main__':
    main(); 
    
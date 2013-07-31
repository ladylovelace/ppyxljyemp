import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", 12000), Handler)

print("AW YEAHH! WE'RE BACK")
httpd.serve_forever()
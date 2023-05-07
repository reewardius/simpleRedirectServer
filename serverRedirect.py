#!/usr/bin/env python3

import sys
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import request, parse

class Redirect(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(int(sys.argv[3]) if len(sys.argv) == 4 else 302)
        self.send_header('Location', sys.argv[2])
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Content-Length': str(len(post_data))}
        req = request.Request(sys.argv[2], post_data, headers, method='POST')
        response = request.urlopen(req)
        self.send_response(response.status)
        for header in response.headers:
            self.send_header(header, response.headers[header])
        self.end_headers()
        self.wfile.write(response.read())

    def log_message(self, format, *args):
        return

if len(sys.argv) != 3 and len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <port_number> <url> [status_code]")
    sys.exit(1)

try:
    server_address = ('', int(sys.argv[1]))
    httpd = HTTPServer(server_address, Redirect)
    print(f"Serving on port {sys.argv[1]}...")
    httpd.serve_forever()
except socket.error as e:
    print(f"Error: {e}")
    sys.exit(1)

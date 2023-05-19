from http.server import BaseHTTPRequestHandler, HTTPServer

class DummyServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, DummyServerRequestHandler)
    print('Server running on http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

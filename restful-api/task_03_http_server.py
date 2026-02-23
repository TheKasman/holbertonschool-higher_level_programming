#!/usr/bin/python3
"""time to work on the http.server"""
import http.server
import json

PORT = 8000


class Handler(http.server.BaseHTTPRequestHandler):
    """A handler for the server, hey pard!"""

    def do_GET(self):
        """It's the do get. thing.."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: This endpoint does not exist.")


server_address = ('', PORT)
httpd = http.server.HTTPServer(server_address, Handler)
print(f"Server running on port {PORT}...")
httpd.serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        page = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>DevOps Virtual Lab</title>
            <style>
                body { font-family: Arial; text-align: center; margin-top: 100px; }
                h1 { color: #2563eb; }
            </style>
        </head>
        <body>
            <h1>DevOps CI/CD Pipeline</h1>
            <p>Application is running successfully!</p>
            <p>demonstrating our deployement !!!!</p>
            <p>automatically Deployed by github actions ;).</p>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(page.encode())

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()

#!/usr/bin/env python3
"""
Simple HTTP server to serve the mitzvot HTML files locally.
This avoids CORS issues when loading JSON data.
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

def serve_files():
    """Start a local HTTP server to serve the files."""
    
    # Change to the directory containing the files
    os.chdir('/Users/aaronhayden/Desktop/613')
    
    PORT = 8000
    
    # Create a custom handler that serves files with proper MIME types
    class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            # Add CORS headers to allow cross-origin requests
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            super().end_headers()
    
    # Start the server
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print(f"Serving files from: {os.getcwd()}")
        print("\nAvailable files:")
        print(f"   - Static HTML: http://localhost:{PORT}/613_mitzvot_table.html")
        print(f"   - Dynamic HTML: http://localhost:{PORT}/613_mitzvot_dynamic.html")
        print(f"   - JSON Data: http://localhost:{PORT}/mitzvot_data.json")
        print("\nOpening dynamic version in browser...")

        # Open the dynamic version in the browser
        webbrowser.open(f'http://localhost:{PORT}/613_mitzvot_dynamic.html')

        print("\nPress Ctrl+C to stop the server")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    serve_files()

"""
Smart Quiz - Windows Production WSGI Server (Waitress)
Runs the Flask application with high concurrency, multi-threading,
and stability for school evaluations, intranet, or presentation hosting.
"""

import os
import socket
from waitress import serve
from app import app, db


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


if __name__ == "__main__":
    local_ip = get_local_ip()
    port = int(os.environ.get("PORT", 5000))

    print("=" * 65)
    print(" [PRODUCTION] Smart Quiz - WSGI Server (Waitress)")
    print(f" Database Engine:         {db.engine.upper()}")
    print(f" Desktop / Local PC:      http://127.0.0.1:{port}")
    print(f" Android / Mobile Device: http://{local_ip}:{port}")
    print("=" * 65)
    print("Serving production traffic with 4 threads. Press CTRL+C to stop.")

    serve(app, host="0.0.0.0", port=port, threads=4)

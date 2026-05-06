#!/usr/bin/env python3
from __future__ import annotations

import argparse
import http.server
import socketserver
from pathlib import Path


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Serve the AzureDust static site locally for preview."
    )
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to.")
    parser.add_argument("--port", type=int, default=4173, help="Port to serve on.")
    parser.add_argument(
        "--dir",
        default=str(Path(__file__).resolve().parent.parent),
        help="Directory to serve.",
    )
    args = parser.parse_args()

    directory = Path(args.dir).resolve()
    handler = lambda *handler_args, **handler_kwargs: http.server.SimpleHTTPRequestHandler(  # noqa: E731
        *handler_args, directory=str(directory), **handler_kwargs
    )

    with ReusableTCPServer((args.host, args.port), handler) as httpd:
        print(f"Preview server running at http://{args.host}:{args.port}")
        print(f"Serving directory: {directory}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nPreview server stopped.")


if __name__ == "__main__":
    main()

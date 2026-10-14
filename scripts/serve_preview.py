"""Serve the built static site at its project path for local browser verification."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import yaml

ROOT=Path(__file__).resolve().parents[1]
PREFIX=urlparse(yaml.safe_load((ROOT/'mkdocs.yml').read_text(encoding='utf-8'))['site_url']).path.rstrip('/')


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == PREFIX or self.path.startswith(PREFIX+'/'):
            self.path=self.path[len(PREFIX):] or '/'
        super().do_GET()

    def log_message(self,*args):
        pass


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--port',type=int,default=8771)
    args=parser.parse_args()
    ThreadingHTTPServer(('127.0.0.1',args.port),partial(Handler,directory=str(ROOT/'site'))).serve_forever()

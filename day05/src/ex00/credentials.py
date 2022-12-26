from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape
import json
from db import db

def app(environ, start_response):
    query = parse_qs(environ["QUERY_STRING"])
    _species = escape(''.join([escape(i) for i in query.get('species', ['none'])]))
    species = db.get(_species)
    _resp = {'credentials': species or 'Unknown'}

    response = json.dumps(_resp)

    response_headers =  [
        ('Content-Type', 'application/json'),
        ('Content-length', str(len(response)))
    ]

    start_response("200 OK" if species else "404 NOT FOUND", response_headers)
    return [response.encode()]

httpd = make_server('localhost', 8888, app)

httpd.serve_forever()

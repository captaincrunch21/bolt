
import cgi
import mimetypes
import os
import re
import random
import Cookie
import threading
try:
    from urlparse import parse_qs
except ImportError:
    from cgi import parse_qs


DEBUG = False
OPTIMIZER = True
ROUTES_SIMPLE = {}
ROUTES_REGEXP = {}
ERROR_HANDLER = {}
HTTP_CODES = {
    100: 'CONTINUE',
    101: 'SWITCHING PROTOCOLS',
    200: 'OK',
    201: 'CREATED',
    202: 'ACCEPTED',
    203: 'NON-AUTHORITATIVE INFORMATION',
    204: 'NO CONTENT',
    205: 'RESET CONTENT',
    206: 'PARTIAL CONTENT',
    300: 'MULTIPLE CHOICES',
    301: 'MOVED PERMANENTLY',
    302: 'FOUND',
    303: 'SEE OTHER',
    304: 'NOT MODIFIED',
    305: 'USE PROXY',
    306: 'RESERVED',
    307: 'TEMPORARY REDIRECT',
    400: 'BAD REQUEST',
    401: 'UNAUTHORIZED',
    402: 'PAYMENT REQUIRED',
    403: 'FORBIDDEN',
    404: 'NOT FOUND',
    405: 'METHOD NOT ALLOWED',
    406: 'NOT ACCEPTABLE',
    407: 'PROXY AUTHENTICATION REQUIRED',
    408: 'REQUEST TIMEOUT',
    409: 'CONFLICT',
    410: 'GONE',
    411: 'LENGTH REQUIRED',
    412: 'PRECONDITION FAILED',
    413: 'REQUEST ENTITY TOO LARGE',
    414: 'REQUEST-URI TOO LONG',
    415: 'UNSUPPORTED MEDIA TYPE',
    416: 'REQUESTED RANGE NOT SATISFIABLE',
    417: 'EXPECTATION FAILED',
    500: 'INTERNAL SERVER ERROR',
    501: 'NOT IMPLEMENTED',
    502: 'BAD GATEWAY',
    503: 'SERVICE UNAVAILABLE',
    504: 'GATEWAY TIMEOUT',
    505: 'HTTP VERSION NOT SUPPORTED',
}


class ServerAdapter(object):
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = int(port)
        self.options = kargs
0
    def __repr__(self):
        return "%s (%s:%d)" % (self.__class__.__name__, self.host, self.port)

    def run(self, handler):
        pass

class WSGIRefServer(ServerAdapter):
    def run(self, handler):
        from wsgiref.simple_server import make_server
        srv = make_server(self.host, self.port, handler)
        srv.serve_forever()


def run(server=WSGIRefServer, host='127.0.0.1', port=8080,):
    if isinstance(server, type) and issubclass(server, ServerAdapter):
        server = server(host=host, port=port)

    print 'Bolt server starting up (using %s)...' % repr(server)
    print 'Listening on http://%s:%d/' % (server.host, server.port)
    print 'Use Ctrl-C to quit.'
    print

    try:
        server.run(WSGIHandler)
    except KeyboardInterrupt:
        print "Shuting down..."






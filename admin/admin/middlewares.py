# middleware_sample/middlewares.py 
from rest_framework.request import Request
import json
from products import *
import time

correlation_id = ''

class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: Request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        global correlation_id
        correlation_id = request.headers.get('X-My-Correlation-Id')
        if correlation_id is None:
            correlation_id = "admin-" + str(int(time.time()))
        headers = str(request.headers).replace("'", '"')
        body = bytes(request.body).replace(b"'", b'"')
        if body.decode('utf-8') == '':
            body = '{}'
        req = {
            "header": json.loads(headers),
            "body": json.loads(body),
            "path": request.path,
            "method": request.method,
            "correlation_id": correlation_id,
        }
        publish_log("str", req)
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response



# middleware_sample/middlewares.py 
from rest_framework.request import Request
import json
from products import *


class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: Request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        headers = str(request.headers).replace("'", '"')
        body = bytes(request.body).replace(b"'", b'"')
        if body.decode('utf-8') == '':
            body = '{}'
        req = {
            "header": json.loads(headers),
            "body": json.loads(body)
        }
        publish_log("str", req)
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response



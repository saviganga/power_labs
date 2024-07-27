from django.http import JsonResponse
import logging


class Handle404ErrorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if response.status_code == 404:
            return JsonResponse({'status': 'FAILED', 'message': 'Oops! This page cannot be found'}, status=404)
        return response
    

class Handle403ErrorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if response.status_code == 403:
            return JsonResponse({'status': 'FAILED', 'message': 'Oops! You do not have permission to view this resource'}, status=403)
        return response
    
logger = logging.getLogger('django')

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Process the request and get the response
        response = self.get_response(request)

        # Log the end of the request and response
        if response.status_code > 400:
            logger.error("Request failed: %s %s, Status code: %s", request.method, request.path, response.status_code)

        return response

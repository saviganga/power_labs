from django.http import JsonResponse

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
# middleware.py
from django.utils import translation

class ForceEnglishMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        translation.activate('en')  # Activate English globally
        response = self.get_response(request)
        return response

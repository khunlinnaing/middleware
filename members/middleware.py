import datetime
from django.http import HttpResponse
def timing(get_response):
    def middleware(request):
        request.current_time = datetime.datetime.now()
        response = get_response(request)
        return response
    
    # def process_view(request, view_func, view_args, view_kwargs):
    #     return HttpResponse("hello")
    
    # middleware.process_view = process_view

    def process_exception(request, exception):
        return HttpResponse("There was an error")
    
    middleware.process_exception = process_exception
    return middleware

# class Timing:
#     def __init__(self, get_response):
#         self.get_response = get_response
    
#     def __call__(self, request):
#         request.current_time = datetime.datetime.now()
#         response = self.get_response(request)
#         return response
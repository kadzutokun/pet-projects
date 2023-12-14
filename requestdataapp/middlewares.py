from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import time


# def set_useragent_on_request_middleware(get_response):
#     def middleware(request : HttpRequest):
#         response = get_response(request)
#         return response

#     return middleware()


# class CountRequestsMiddleware:
#     def __init__(self, get_response):
#         self.request_count = 0
#         self.request_time = {}
#         self.get_response = get_response


#     def __call__(self, request: HttpRequest):
#         self.request_count += 1
#         time_delay = 10
#         if not self.request_time:
#             print('Словарь еще пуст')
#         else:
#             if (round(time.time()) * 1 ) - self.request_time['time'] < time_delay and self.request_time['ip_address'] == request.META.get('REMOTE_ADDR'):
#                 print('Похоже на Ddos :C')
#             return render(request, 'requestdataapp/error-request.html')
#         self.request_time = {'time': round(time.time()) * 1, 'ip_address': request.META.get('REMOTE_ADDR')}
#         self.request_count +=1 
#         response = self.get_response(request)
#         return response
        


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('myapp/index.html', {}); 

def main(request):
    return HttpResponse("<h1>Hello, django (appengine)</h1>");
   


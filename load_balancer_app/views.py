from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import socket

# Create your views here.
def index(request):

    return HttpResponse(f"<h1>Request from: {socket.gethostname()}</>")
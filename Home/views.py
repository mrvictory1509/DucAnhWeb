from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.db import connection
from django.contrib.auth import login
import base64
import string
import random
import pickle
import os
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google_auth_oauthlib.flow import InstalledAppFlow
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
def products(request):
    return render(request, 'products.html')
def sales(request):
    return render(request, 'sales.html')
def contacts(request):
    return render(request, 'contacts.html')
def about_us(request):
    return render(request, 'about_us.html')
def sign_in(request):
    return render(request, 'sign_in.html')
def sign_up(request):
    return render(request, 'sign_up.html')
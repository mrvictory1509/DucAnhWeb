from django.shortcuts import render, redirect
from .models import User, Category, Sex, Shoes, Cart, Product, Bill
from django.db.models import F
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
from home.form import SignUpForm
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse

def index(request):
    
    return render(request, 'index.html')

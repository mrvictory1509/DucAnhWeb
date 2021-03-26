from Home.models import Vests, Category, Cart, Bill, User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.db import connection
from django.contrib.auth import login
import base64
import string
import random
import pickle
import os
from django.db.models import F
from Home.form import SignUpForm
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
    if request.user.is_authenticated:
        trend = Vests.objects.all().order_by(F('NumberBuy').desc())[:6]
        vests = {'trend' : trend, 'setToolbar':['home.html', request.user.username]}
        return render(request, 'home.html', vests)
    else:
        trend = Vests.objects.all().order_by(F('NumberBuy').desc())[:6]
        vests = {'trend' : trend, 'setToolbar':'home.html'}
        return render(request, 'home.html', vests)
def products(request):
    if request.user.is_authenticated:
        all = Vests.objects.all()
        vests = {'all' : all, 'setToolbar':['products.html', request.user.username]}
        return render(request, 'products.html', vests)
    else:
        all = Vests.objects.all()
        vests = {'all' : all, 'setToolbar':'products.html'}
        return render(request, 'products.html', vests)
def sales(request):
    if request.user.is_authenticated:
        sale = Vests.objects.filter(Sales = True)
        vests = {'sale' : sale, 'setToolbar':['sales.html', request.user.username]}
        return render(request, 'sales.html', vests)
    else:
        sale = Vests.objects.filter(Sales = True)
        vests = {'sale' : sale, 'setToolbar':['sales.html']}
        return render(request, 'sales.html', vests) 
def vests(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.id, home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price, home_vests.Image FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Vests'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':['vests.html', request.user.username]}
        return render(request, 'vests.html', vests)
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Vests'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':'vests.html'}
        return render(request, 'vests.html', vests)
def Pants(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.id, home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price, home_vests.Image FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Pants'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':['Pants.html', request.user.username]}
        return render(request, 'Pants.html', vests)
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Pants'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':'Pants.html'}
        return render(request, 'Pants.html', vests)
def Belts(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.id, home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price, home_vests.Image FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Belts'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':['Belts.html', request.user.username]}
        return render(request, 'Belts.html', vests)
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Belts'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':'Belts.html'}
        return render(request, 'Belts.html', vests)
def Shoes(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.id, home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price, home_vests.Image FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Shoes'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':['Shoes.html', request.user.username]}
        return render(request, 'Shoes.html', vests)
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Shoes'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':'Shoes.html'}
        return render(request, 'Shoes.html', vests)
def Shirts(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.id, home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price, home_vests.Image FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Shirts'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':['Shirts.html', request.user.username]}
        return render(request, 'Shirts.html', vests)
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Shirts'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':'Shirts.html'}
        return render(request, 'Shirts.html', vests)
def Ties(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.id, home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price, home_vests.Image FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Ties'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':['Ties.html', request.user.username]}
        return render(request, 'Ties.html', vests)
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.Name, home_vests.Price, home_vests.NumberBuy, home_vests.Sales, home_vests.New_Price FROM home_vests INNER JOIN home_category ON home_vests.CategoryID_id = home_category.id WHERE home_category.Name = 'Ties'"
            )
            vest = cursor.fetchall()
        vests = {'vest' : vest, 'setToolbar':'Ties.html'}
        return render(request, 'Ties.html', vests)
def View(request, id):
    if request.user.is_authenticated:
        view = Vests.objects.filter(id = id)
        vests = {'view' : view, 'setToolbar':['product_detail.html', request.user.username]}
        return render(request, 'product_detail.html', vests)
    else:
        view = Vests.objects.filter(id = id)
        vests = {'view' : view, 'setToolbar':'product_detail.html'}
        return render(request, 'product_detail.html', vests)
def about_us(request):
    return render(request, 'about_us.html')
def sign_in(request):
    return render(request, 'sign_in.html')
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})
def Cart(request):
    if request.user.is_authenticated:
        return render(request, 'shopping_Cart.html')
    else:
         return render(request, 'sign_in.html')
def add_Cart(request, id):
    if request.user.is_authenticated:
        lenCart = len(Cart.objects.filter(UserID_id= request.user.id, VestsID_id= id))
        if lenCart > 0:
            QTY = Cart.objects.filter(UserID_id= request.user.id, VestsID_id= id)[0].Quantity
            Cart.objects.filter(UserID_id=request.user.id, VestsID_id= id).update(Quantity= QTY + 1)
            response = HttpResponse()
            response.writelines('Add to Cart successfully')
            return response
        else:
            NameCart = request.user.username
            Cart.objects.create(UserID_id= request.user.id, VestsID_id= id , Quantity= 1, Name= NameCart)
            response = HttpResponse()
            response.writelines('Add to Cart successfully')
            return response    
    else:
        response = HttpResponse()
        response.writelines('Login')
        return response

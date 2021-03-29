from .models import Vests, Category, CartUser, BillUser, User, UserInformation
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
from .form import SignUpForm
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google_auth_oauthlib.flow import InstalledAppFlow
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.core.files.base import ContentFile

def home(request):
    if request.user.is_authenticated:
        trend = Vests.objects.all().order_by(F('NumberBuy').desc())[:6]
        vests = {'trend' : trend, 'setToolbar': request.user.username}
        return render(request, 'home.html', vests)
    else:
        trend = Vests.objects.all().order_by(F('NumberBuy').desc())[:6]
        vests = {'trend' : trend, 'setToolbar': request.user.username}
        return render(request, 'home.html', vests)
def Search(request, Name):
    if request.user.is_authenticated:
        trend = Vests.objects.filter(Name__contains = Name)
        vests = {'trend' : trend, 'setToolbar': request.user.username}
        return render(request, 'home.html', vests)
    else:
        trend = Vests.objects.filter(Name__contains = Name)
        vests = {'trend' : trend, 'setToolbar': request.user.username}
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
def sign_upInterface(request):
    return render(request, 'sign_up.html')
def sign_up(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName','')
        lastName = request.POST.get('lastName','')
        Username = request.POST.get('Username','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        DOB = request.POST.get('DOB','')
        phoneNumber = request.POST.get('phoneNumber','')
        height = request.POST.get('height','')
        weight = request.POST.get('weight','')
        Gender = request.POST.get('Gender','')
        User.objects.create_user(password = password, username = Username, first_name = firstName, last_name = lastName, email = email, is_active = True,  is_superuser = False, is_staff = False)
        UserInformation.objects.create(UserID_id = User.objects.latest('id').id, Phone = phoneNumber, Height = height, Weight = weight, DOB = DOB, Gender = Gender)
        return redirect('/sign_in')
    else:
        return redirect('/sign_in')
def Cart(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT home_vests.Name, home_vests.Image, home_vests.Price, home_cartuser.Quantity, home_cartuser.id FROM home_vests INNER JOIN home_cartuser ON home_vests.id = home_cartuser.VestsID_id INNER JOIN auth_user ON auth_user.id = home_cartuser.UserID_id WHERE auth_user.id = '%s'",
                [request.user.id]
            )
            viewCart = cursor.fetchall()
        return render(request, 'shopping_Cart.html', {"viewCart":viewCart})
    else:
         return render(request, 'sign_in.html')
def login(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = authenticate(username=username, password=password)
            if(user is not None):
                request.session.set_expiry(86400)
                auth_login(request, user)
                return redirect('/home')
            else:
                return render(request, 'sign_in.html', {'error':'Account or password is incorrect'})
        else:
            return redirect('/sign_in')
def logout(request):
    django_logout(request)
    return redirect('/home')
def addCart(request, id):
    if request.user.is_authenticated:
        if len(CartUser.objects.filter(UserID_id = request.user.id,VestsID_id = id)) == 0:
            CartUser.objects.create(UserID_id = request.user.id,VestsID_id = id, Quantity = 1)
            return HttpResponse("Add to Cart successfully")
        else:
            Quantity = CartUser.objects.filter(UserID_id = request.user.id,VestsID_id = id)[0].Quantity
            CartUser.objects.filter(UserID_id = request.user.id,VestsID_id = id).update(Quantity = Quantity + 1)
            return HttpResponse("Add to Cart successfully")
    else:
        return HttpResponse("Login")
def setQuality(request, CartID, Quanlity):
    if request.user.is_authenticated:
        CartUser.objects.filter(id = CartID).update(Quantity = Quanlity)
        return HttpResponse("Successfully")
    else:
        return HttpResponse("Login")
def checkout(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute(
                " SELECT home_vests.Name, home_vests.Image, home_vests.Price, home_cartuser.Quantity, home_cartuser.id FROM home_vests INNER JOIN home_cartuser ON home_vests.id = home_cartuser.UserID_id INNER JOIN auth_user ON auth_user.id = home_cartuser.UserID_id WHERE auth_user.id = '%s'",
                [request.user.id]
            )
            viewCart = cursor.fetchall()
        return render(request, 'checkout.html', {"viewCart":viewCart})
    else:
        return HttpResponse("Login")
def setBill(request):
    if request.user.is_authenticated:
        bill = request.POST.get('ImageBill')
        format, imgstr = bill.split(';base64,') 
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        CartUser.objects.filter(UserID_id = request.user.id).delete()
        BillUser.objects.create(UserID_id =request.user.id, Ship = False, Image = data)
        return redirect('/home')
    else:
        return redirect('/sign_in')
def yourOrder(request):
    if request.user.is_authenticated:
        bill = BillUser.objects.filter(UserID_id =request.user.id).order_by('-Date')
        return render(request, 'yourOrder.html', {'bill':bill})
    else:
        return redirect('/sign_in')

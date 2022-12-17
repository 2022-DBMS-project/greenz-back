from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import NotFound
from django.db import connection
from django.contrib import messages
from greenz.models import *


# from .models import RMAP, CartItem, Cart, Orders, Product
from django.views import View



# main page
def main(request):
    if request.COOKIES.get('id'):
        return render(request, 'main.html', context={'text': 'Logout'})
    else:
        return render(request, 'main.html', context={'text': 'Login'})


# product list page(디폴트는 fresh food 리스트를 보여주는 페이지)
def product(request):
    product = FreshFoodList.objects.all()

    if request.COOKIES.get('id'):
        text = 'Logout'
    else:
        text = 'Login'

    return render(request, 'freshfood.html', context={'text': text, 'food_list': product})


def source(request):
    if request.COOKIES.get('id'):
        return render(request, 'source.html', context={'text': 'Logout'})
    else:
        return render(request, 'source.html', context={'text': 'Login'})


def freshfood(request, product_id):
    try:
        product = FreshFoodList.objects.get(id=product_id)
    except Product.DoesNotExist:
        product = None

    if product is None:
        raise NotFound("페이지를 찾을 수 없습니다.")

    if request.COOKIES.get('id'):
        text = 'Logout'
    else:
        text = 'Login'

    return render(request, 'product.html', context={'text': text, 'fresh_food': product})


# recipe list page
def recipe(request):
    if request.COOKIES.get('id'):
        return render(request, 'Recipe_List.html', context={'text': 'Logout'})
    else:
        return render(request, 'Recipe_List.html', context={'text': 'Login'})


# restaurant list page
def restaurant(request):
    info_res = RMAP.objects.all()  # RMAP data 불러오기
    if request.COOKIES.get('id'):
        return render(request, 'Restaurant_map.html', context={'text': 'Logout'})
    else:
        return render(request, 'Restaurant_map.html', context={'text': 'Login', 'info_res': info_res})



# cart page
def cart(request):
    if request.COOKIES.get('id'):
        return render(request, 'cart.html', context={'text': 'Logout'})
    else:
        messages.add_message(request, messages.ERROR, '권한이 없습니다. 로그인해주세요.')
        return render(request, 'login.html', context={'text': 'Login'})


def mypage(request):
    if request.COOKIES.get('id'):
        return render(request, 'mypage.html', context={'text': 'Logout'})
    else:
        messages.add_message(request, messages.ERROR, '권한이 없습니다. 로그인해주세요.')
        return render(request, 'login.html', context={'text': 'Login'})


@csrf_exempt
def join_view(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        phone_number = request.POST.get("phone_number")

        # User 모델 가져오기
        user = User()
        user.id = id
        user.name = name
        user.email = email
        user.password = password
        user.address = address
        user.phone_number = phone_number

        # db에 저장
        user.save()

    return render(request, 'main.html')



# login page
@csrf_exempt
def login(request):
    if request.COOKIES.get('id'):
        messages.add_message(request, messages.INFO, '로그아웃 되었습니다.')
        response = render(request, 'main.html', context={'text': 'Login'})
        response.delete_cookie('id')
        return response
    else:
        return render(request, 'login.html', context={'text': 'Login'})


@csrf_exempt
def login_view(request):
    id = request.POST.get("id")
    password = request.POST.get("password")

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        user = None

    if user is None:
        messages.add_message(request, messages.WARNING, '아이디가 잘못되었습니다. 다시 입력해주세요.')
        return render(request, 'login.html', context={'text': 'Login'})

    if user.password == password:
        response = render(request, 'main.html', context={'text': 'Logout'})
        response.set_cookie('id', id)
        return response
    else:
        messages.add_message(request, messages.WARNING, '비밀번호가 잘못되었습니다.')
        return render(request, 'login.html', context={'text': 'Login'})

def get_post(request):
    global store

    store_id = request.GET.get('id', None)
    store = RMAP.objects.get(name=store_id)

    return render(request, 'Restaurant2.html', context={'store': store})


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return  cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id= _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()


    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request, total=2000, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.cost * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', dict(cart_items = cart_items, total = total, counter = counter))


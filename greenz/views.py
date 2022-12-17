from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import AuthenticationFailed
from django.db import connection
from django.contrib import messages
from greenz.models import User


# main page
def main(request):
    if request.COOKIES.get('id'):
        return render(request, 'main.html', context={'text': 'Logout'})
    else:
        return render(request, 'main.html', context={'text': 'Login'})


# product list page(디폴트는 fresh food 리스트를 보여주는 페이지)
def product(request):
    if request.COOKIES.get('id'):
        return render(request, 'freshfood.html', context={'text': 'Logout'})
    else:
        return render(request, 'freshfood.html', context={'text': 'Login'})


# recipe list page
def recipe(request):
    if request.COOKIES.get('id'):
        return render(request, 'Recipe_List.html', context={'text': 'Logout'})
    else:
        return render(request, 'Recipe_List.html', context={'text': 'Login'})


# restaurant list page
def restaurant(request):
    if request.COOKIES.get('id'):
        return render(request, 'Restaurant_map.html', context={'text': 'Logout'})
    else:
        return render(request, 'Restaurant_map.html', context={'text': 'Login'})


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

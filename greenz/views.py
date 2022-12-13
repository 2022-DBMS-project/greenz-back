from django.shortcuts import render


# main page
def main(request):
    return render(request, 'main.html')


# product list page(디폴트는 fresh food 리스트를 보여주는 페이지)
def product(request):
    return render(request, 'freshfood.html')


# recipe list page
def recipe(request):
    return render(request, 'Recipe_List.html')


# restaurant list page
def restaurant(request):
    return render(request, 'Restaurant_map.html')


# cart page
def cart(request):
    return render(request, 'cart.html')


# my page
def mypage(request):
    return render(request, 'mypage.html')


# login page
def login(request):
    return render(request, 'login.html')

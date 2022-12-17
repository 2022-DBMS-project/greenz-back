from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name='index'),
    path('product/', views.product, name='product_list'),
    path('recipe/', views.recipe, name='recipe_list'),
    path('restaurant/', views.restaurant, name='restaurant_list'),
    path('cart/', views.cart, name='cart'),
    path('mypage/', views.mypage, name='mypage'),
    path('login/', views.login, name='login'),
    path('join_view', views.join_view, name='join'),
    path('login_view', views.login_view, name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

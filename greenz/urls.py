from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name='index'),
    path('product/', views.product, name='food_list'),
    path('source/', views.source, name='source_list'),
    path('freshfood/<int:product_id>', views.freshfood, name='freshfood'),
    path('recipe/', views.recipe, name='recipe_list'),
    path('restaurant/', views.restaurant, name='restaurant_list'),
    path('restaurant2/', views.get_post, name='restaurant2'),
    path('cart/', views.cart, name='cart'),
    path('mypage/', views.mypage, name='mypage'),
    path('login/', views.login, name='login'),
    path('join_view', views.join_view, name='join'),
    path('login_view', views.login_view, name='login'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
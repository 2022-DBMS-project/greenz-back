from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "cart"

urlpatterns = [
    path('', views.main, name='index'),
    path('product/', views.product, name='food_list'),
    path('source/', views.source, name='source_list'),
    path('food/<int:product_id>', views.food, name='freshfood'),
    path('recipe/', views.recipe, name='recipe_list'),
    path('recipe_detail/<int:recipe_id>', views.recipe_detail, name='recipe_list'),
    path('restaurant/', views.restaurant, name='restaurant_list'),
    path('list_restaurant/<int:rmap_id>', views.list_restaurant, name='list_restaurant'),
    path('cart/', views.cart, name='cart'),
    path('mypage/', views.mypage, name='mypage'),
    path('login/', views.login, name='login'),
    path('join_view', views.join_view, name='join'),
    path('login_view', views.login_view, name='login'),
    path('add/<int:product_id>', views.add_cart, name='add_cart'),
    path('edit/', views.edit, name='edit'),
    path('buy/<int:cart_id>', views.order, name='order'),
    path('order/<int:cart_id>', views.order_detail, name='order')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name='store'),

    path('product/<int:id>/', views.product_detail),

    path('cart/', views.cart),

    path('checkout/', views.checkout),

    path('my-orders/', views.my_orders),

    path('login/', views.login_view),

    path('logout/', views.logout_view),

    path('register/', views.register),

    path('wishlist/', views.wishlist),

]
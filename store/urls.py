from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('forget/', views.forget_password, name='forget'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('offer/', views.offer_page, name='offer'),
]

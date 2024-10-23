from django.urls import path
from app1 import views

urlpatterns=[
    path('home',views.home,name="homepage"),
    path('contact',views.contact,name="contactpage"),
    path('about',views.about,name='aboutpage'),
    path('help',views.help,name="help_page"),
    path('check/<int:num>',views.func,name="evenodd"),
    path('ispalindrome/<str:sname>',views.func2,name="palindrome"),
    path('signUp',views.signUp,name="register")
]
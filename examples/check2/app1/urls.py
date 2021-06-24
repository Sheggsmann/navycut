from navycut.urls import path, url
from . import views

url_patterns = [
    path("" , views.IndexView, "index"),
    path("/register", views.AuthView, "auth"),
    url("/home", views.home, "home"),
    url("/mail", views.send_email, "mail")
]
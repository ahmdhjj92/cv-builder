from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('header/', views.header, name="header"),
    path('work/', views.work_experience, name="work"),
    path('summary/', views.summary, name="summary"),

]

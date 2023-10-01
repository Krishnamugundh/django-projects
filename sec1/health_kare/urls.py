from django.urls import path
from . import views

urlpatterns =[
    path('login/',views.login_doc,name='login'),
    path('',views.hello,name='home'),
    path('create/',views.createPat,name='PatCreate'),
    path('create-user/',views.createNew,name='user'),
]
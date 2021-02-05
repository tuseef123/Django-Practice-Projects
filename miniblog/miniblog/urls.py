
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from blog import views

handler404 = views.handler404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.user_signup,name='signup'),
    path('addpost/',views.add_post,name = 'addpost'),
    path('updatepost/<int:pk>/',views.update_post,name= 'updatepost'),
    path('delete/<int:pk>/',views.delete_post,name = 'deletepost'),
]

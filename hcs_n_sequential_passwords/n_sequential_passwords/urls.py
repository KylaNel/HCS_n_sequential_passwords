from django.urls import path
from n_sequential_passwords import views

app_name = 'n_sequential_passwords'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('pin/', views.pin_login, name='pin'),
    path('pattern_lock/', views.pattern_lock, name="pattern_lock"),
    path('start/', views.start, name="start"),
    path('password_1/', views.password_1_view, name="password_1"),
    path('pin_1/', views.pin_1_view, name="pin_1"),
    path('success/', views.success, name='success'),
]
from django.urls import path
from n_sequential_passwords import views

app_name = 'n_sequential_passwords'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('pin/', views.pin_view, name='pin'),
    path('password/', views.password_view, name='password'),
    path('pattern_lock/', views.pattern_lock, name="pattern_lock"),
    path('start/', views.start, name="start"),
    path('password_1/', views.password_1_view, name="password_1"),
    path('pin_1/', views.pin_1_view, name="pin_1"),
    path('password_2_1/', views.password_2_view_1, name="password_2_1"),
    path('pin_2/', views.pin_2_view, name="pin_2"),
    path('password_2_2/', views.password_2_view_2, name="password_2_2"),
    path('success/', views.success, name='success'),
    path('start/', views.start, name="start"),
    path('timer/', views.timer, name='timer_view'),
    path('prompt/', views.prompt, name='promt'),
]
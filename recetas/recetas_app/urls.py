from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lista_recetas, name='lista_recetas'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('subir/', views.subir_receta, name='subir_receta'),
    path('login/', auth_views.LoginView.as_view(template_name='recetas_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='recetas_app/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('receta/<int:pk>/', views.detalle_receta, name='detalle_receta'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]

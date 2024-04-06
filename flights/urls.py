from django.urls import path
from .views import flight_list, dashboard, flight_create, flight_update, flight_delete, about
from django.contrib.auth.views import LogoutView# Import dashboard from views
from . import views

urlpatterns = [
    path('', flight_list, name='flight_list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', flight_create, name='flight_create'),
    path('update/<int:pk>/', flight_update, name='flight_update'),
    path('delete/<int:pk>/', flight_delete, name='flight_delete'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('about/', about, name='about'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    # Add this to your urls.py
    path('logout/', views.logout_user, name='logout'),

]
    # Add more paths for create, update, delete


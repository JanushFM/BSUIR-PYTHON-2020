from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_of_artists, name='home'),
    path('album/<str:artist_name>/', views.album, name='album'),
    path('biography/<str:artist_name>/', views.biography, name='biography'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),

    path('update_order/<str:order_id>/', views.update_order, name="update_order"),
    path('create_order/<str:order_id>/', views.create_order, name='create_order'),
    path('delete_order/<str:order_id>/', views.delete_order, name="delete_order"),

    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('account/', views.profile_page, name="account"),
    path('email/', views.send_message),
    path('activate/<uidb64>/<token>/', views.activate_account, name="activate")
]

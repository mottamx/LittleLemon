from . import views
from django.urls import include, path
from .views import MenuItemsView, SingleMenuItemView, UserListView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('users/', UserListView.as_view(), name='user-list'),
]

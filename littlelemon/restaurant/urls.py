from . import views
from django.urls import include, path
from .views import MenuItemsView, SingleMenuItemView

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

from django.urls import path

from App import views

urlpatterns = [
    path('login_view', views.login_view, name='login_view'),
    path('dash', views.dash, name='dash'),
    path('page_one', views.page_one, name='page_one'),
    path('page_two', views.page_two, name='page_two'),
]

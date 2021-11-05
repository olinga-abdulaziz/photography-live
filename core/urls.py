from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('potforlio',views.PotforlioView.as_view(),name='potforlio'),
    path('add-post',views.AddpostView.as_view(),name='addpost'),
]
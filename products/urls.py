from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'), 
    path('code_auditing', views.code_auditing, name='code_auditing'), 
]
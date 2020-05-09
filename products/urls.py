from django.urls import path

from . import views

urlpatterns = [
    #This would be a comment in Python
    path('', views.index, name='index'),
    
    #This would be a comment in Python
    path('web_design', views.web_design, name='web_design'), 
    path('graphics_design', views.graphics_design, name='graphics_design'), 
    path('code_auditing', views.code_auditing, name='code_auditing'),
    path('photography', views.photography, name='photography'), 
    
    #This would be a comment in Python
    path('blog', views.blog, name='blog'), 
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),  
    
        
    #This would be a comment in Python
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
]
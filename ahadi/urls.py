from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog'),
    path('cv-formatting/', views.cv-formatting, name="cv-formatting"),
    path('executive-search/', views.executive-search, name="executive-search"),
    path('job-board/', views.job-board, name="job-board"),
    path('pricing/', views.pricing, name="pricing"),
    path('project-based-hiring/', views.project-based-hiring, name="project-based-hiring"),
    path('rpo-services/', views.rpo-services, name="rpo-services"),
    path('ahadi/', views.traffic_monitor, name="ahadi"), #traffic
    path('what-we-do/', views.what-we-do, name="what-we-do"),
    path('who-we-are/', views.who-we-are, name="who-we-are"),
]
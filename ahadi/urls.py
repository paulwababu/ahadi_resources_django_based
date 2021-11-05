from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog'),
    path('cv-formatting/', views.cvformatting, name="cv-formatting"),
    path('executive-search/', views.executivesearch, name="executive-search"),
    path('job-board/', views.jobboard, name="job-board"),
    path('pricing/', views.pricing, name="pricing"),
    path('project-based-hiring/', views.projectbasedhiring, name="project-based-hiring"),
    path('rpo-services/', views.rposervices, name="rpo-services"),
    path('ahadi/', views.traffic_monitor, name="ahadi"), #traffic
    path('what-we-do/', views.whatwedo, name="what-we-do"),
    path('who-we-are/', views.whoweare, name="who-we-are"),
]
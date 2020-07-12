from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.home , name='home' ),
    path('home', views.home , name='home' ),
    path('contact', views.contact , name='contact' ),
    path('about', views.about , name='about' ),
    path('termsandconditions', views.tnc, name='termsandconditions'),
    path('privacypolicy', views.pp, name='privacypolicy'),
    path('feature', views.fe, name='feature'),
    path('pricing', views.pr, name="pricing"),
 path('sitemap',
         TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml"),name='sitemap'),
path('sitemap.xml',
         TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml"),name='sitemap.xml'),

]
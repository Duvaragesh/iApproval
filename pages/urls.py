#
# Author Duvaragesh Kannan
#

from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about-us', views.about, name='about'),
   path('request_list', views.request_list, name='request_list'),
   path('induction', views.training, name='training'),
]
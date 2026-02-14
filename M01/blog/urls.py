#we add this file manauly
from django.urls import path 
from . import views

app_name='blog'

urlpatterns = [
    # path('about/',about),#we added it
    # path('',views.home),
    path('about/',views.about),
    path('',views.post_list,name='post_list'),
    path('<int:id>/',views.post_detail,name='post_detail')
]

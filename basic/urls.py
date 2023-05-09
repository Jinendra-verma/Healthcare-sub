from django.urls import path
from . import views

urlpatterns = [
    path('' , views.Welcome),
    path('disease' , views.Disease_predict),
    # path('info' , views.Disease_info)
    # path('example/<str:variable>/', views.example_view, name='example'),
    path('disease_info' , views.Disease_info),

]

from django.urls import path
from .views import notebook_list, notebook_detail

urlpatterns = [
    path('', notebook_list, name='notebook_list'),
    path('<int:pk>', notebook_detail, name='notebook_detail')
]
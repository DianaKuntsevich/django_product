from django.urls import path, include
from rest_framework import routers

from .views import NotebookListViewSet

router_notebook = routers.SimpleRouter()
router_notebook.register(r'notebook', NotebookListViewSet,)

urlpatterns = [
    path('', include(router_notebook.urls), name='notebooks')
]


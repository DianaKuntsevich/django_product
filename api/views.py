from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from product_app.models import Notebook

from .serializers import NotebookSerializer
from .permisions import IsAdminOrReadOnly

class NotebookListViewSet(ModelViewSet):
    queryset = Notebook.objects.all().prefetch_related('images')
    serializer_class = NotebookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('price', 'producer')
    search_fields = ('battery', 'condition', 'description', 'diagonal', 'hdd_type', 'hdd_volume', 'link', 'os', 'price', 'processor', 'producer', 'ram', 'resolution', 'title', 'video_card')
    ordering_fields = ('price', 'producer')

    permission_classes = IsAdminOrReadOnly,

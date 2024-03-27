from rest_framework import serializers

from product_app.models import Notebook, Image

class NotebookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notebook
        fields = (
            'id',
            'link',
            'title',
            'price',
            'description',
            'producer',
            'diagonal',
            'resolution',
            'os',
            'processor',
            'ram',
            'hdd_type',
            'video_card',
            'hdd_volume',
            'battery',
            'condition',
            'images')
        depth = 1  #подтягивает информацию по связанным классам

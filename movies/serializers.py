from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Moviedata
        fields = ['id','title','duration','rating','typ','img']
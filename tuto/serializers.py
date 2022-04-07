from rest_framework import serializers 
from tuto.models import Tuto
 
 
class TutoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tuto
        fields = ('id',
                  'title',
                  'description',
                  'published')
from rest_framework import serializers
from api.models import BoastRoast

class BoastRoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoastRoast
        fields = ["id", "post_type", "post_content", "date_created", "total_votes"]





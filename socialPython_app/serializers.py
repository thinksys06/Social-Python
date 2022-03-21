
from rest_framework import serializers
from socialPython_app.models import userModel

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields= '__all__'

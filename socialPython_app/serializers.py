
from pyexpat import model
from rest_framework import serializers
from socialPython_app.models import userModel, userProfileModel

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= userProfileModel
        fields= '__all__'

class userSerializer(serializers.ModelSerializer):
    relation = userProfileSerializer(read_only= True, many= True)
    class Meta:
        model = userModel
        fields= '__all__'



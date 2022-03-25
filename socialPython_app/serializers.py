from rest_framework import serializers
from socialPython_app.models import userModel, userProfileModel
import re

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= userProfileModel
        fields= '__all__'

    def validate_gender(self, gender):
        if (re.match(" 'male' | 'female' ", gender) == None):
            raise serializers.ValidationError("gender accepts only 'male|female' values")
        return gender

class userSerializer(serializers.ModelSerializer):
    relation = userProfileSerializer(read_only= True, many= True)
    class Meta:
        model = userModel
        fields= '__all__'

    



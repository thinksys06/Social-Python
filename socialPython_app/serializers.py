
from pyexpat import model
import re
from rest_framework import serializers
from socialPython_app.models import userModel, userProfileModel

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= userProfileModel
        fields= '__all__'

    def validate_gender(self, id):
        if (re.match("^[0-9]+$", id) == None):
            raise serializers.ValidationError("gender accepts only numeric values")
        return id
    

class userSerializer(serializers.ModelSerializer):
    relation = userProfileSerializer(read_only= True, many= True)
    class Meta:
        model = userModel
        fields= '__all__'

    

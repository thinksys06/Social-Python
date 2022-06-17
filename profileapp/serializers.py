from rest_framework import serializers
from . models import Profile,Education


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        #field=['user','name','title','desc','profile_img']
        fields='__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields='__all__'
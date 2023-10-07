from rest_framework import serializers
from .models import Student
from rest_framework.response import Response

class StudentSerializer(serializers.ModelSerializer):
    length_of_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        # fields = ['id', 'name', 'roll', 'city']
        fields = '__all__'

    def get_length_of_name(self, object):
        length = len(object.name)
        return length


    def validate(self, data):
        print('data: ', data)
        # '' (an empty string): This is the default value that will be 
        # returned if the 'name' key is not found in the data dictionary. 
        name = data.get('name', '')
        city = data.get('city', '')
        if name == city:
            raise serializers.ValidationError(
                'Name and city should be different!!'
            )
        if len(name) < 3:
            raise serializers.ValidationError(
                'Name is too short!!'
            )
        else:
            return data
    
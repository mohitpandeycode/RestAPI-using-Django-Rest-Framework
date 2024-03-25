from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['id']
    def validate(self,data):
        if data['age']<18:
            raise serializers.ValidationError({"error":"age can't be less then 18"})
        return data
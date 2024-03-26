from .models import *
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    def validate(self,data):
        if data['age']<18:
            raise serializers.ValidationError({"error":"age can't be less then 18"})
        return data
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        exclude = ['id']


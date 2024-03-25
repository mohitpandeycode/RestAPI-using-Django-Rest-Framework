# How to make Api's using Django Rest Framework🎯
## All the steps to make setup django rest framework...

- Step 1: install django rest framework.
```
pip install djangorestframework
```
- Step 2: add rest framework in setting.py < INSTALLED_APPS=[]
```
INSTALLED_APPS = [
    'rest_framework',
]
```
- Step 3: make your database model and migrate them 
```
python manage.py makemigrations
python manage.py migrate
```
- Step 4: make a serializers.py file in your app and configure that like this
```
from .models import Student  #import database model!
from rest_framework import serializers  #import serializers from rest framework!

#make class of serializer with the model name like this!
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  # Name of model you want to serialize
        exclude = ['id'] # gives data except id
        #if you want all data then you use!
        fields = '__all__'

```
- Step 5: you can make validation in serializer always, not in views.py example..
```
from .models import Student  #import database model!
from rest_framework import serializers  #import serializers from rest framework!

#make class of serializer with the model name like this!
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  # Name of model you want to serialize
        exclude = ['id'] # gives data except id
        #if you want all data then you use!
        fields = '__all__'

    def validate(self,data):
        if data['age']<18:
            raise serializers.ValidationError({"error":"age can't be less then 18"})
        return data
```
- Step 6: Make urls for views functions.
- Step 7: Make your views.py like this for GET method...
```
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer

# Create your views here.
@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs,many=True)
    return Response({'status':200,'payload':serializer.data,'message':"code get success"})

```
- Step 8: Make your views.py like this for POST method...
```
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer

# Create your views here.
@api_view(['POST'])
def student(request):
    serializer = StudentSerializer(data = request.data)
    if not serializer.is_valid():
         return Response({'status':403,'errors':serializer.errors,'message':"Something went wrong!"})
    serializer.save()
    return Response({'status':200,'payload':serializer.data,'message':"code Post success"})

```
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView

# Create your views here.

# by using api views ..................
class StudentAPI(APIView):
    def get(self,request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs,many=True)
        return Response({'status':200,'payload':serializer.data,'message':"code get success"})


    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':"Something went wrong!"})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"code Post success"})

    def put(self,request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(student_obj ,data = request.data)
            if not serializer.is_valid():
                return Response({'status':403,'errors':serializer.errors,'message':"Something went wrong!"})
            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"code Post success"})
        except Exception as e:
            print(e)
            return Response({'status':404,'message':"Invalid id"})
        

    def patch(self,request):
        pass

    def delete(self,request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            student_obj.delete()
            return Response({'status':200,'message':"Data deleted success"})
        except Exception as e:
            print(e)
            return Response({'status':404,'message':"Invalid id"})























# by using API view decorator
# for GET request......
@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs,many=True)
    return Response({'status':200,'payload':serializer.data,'message':"code get success"})

# for POST request......
@api_view(['POST'])
def student(request):
    serializer = StudentSerializer(data = request.data)
    if not serializer.is_valid():
         return Response({'status':403,'errors':serializer.errors,'message':"Something went wrong!"})
    serializer.save()
    return Response({'status':200,'payload':serializer.data,'message':"code Post success"})

# for PUT request......
@api_view(['PUT'])
def studentUpdate(request,id):
    try:
        student_obj = Student.objects.get(id = id)
        serializer = StudentSerializer(student_obj ,data = request.data, partial = True)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':"Something went wrong!"})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"code Post success"})
    except Exception as e:
        return Response({'status':404,'message':"Invalid id"})
        
# for PATCH request......
@api_view(['PATCH'])
def studentUpdateWithpatch(request,id):
    try:
        student_obj = Student.objects.get(id = id)
        serializer = StudentSerializer(student_obj ,data = request.data, partial=True)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':"Something went wrong!"})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"code Post success"})
    except Exception as e:
        print(e)
        return Response({'status':404,'message':"Invalid id"})
        
        
# for DELETE request......
@api_view(['DELETE'])
def deleteStudent(request,id):
    try:
        student_obj = Student.objects.get(id = id)
        student_obj.delete()
        return Response({'status':200,'message':"Data deleted success"})
    except Exception as e:
        print(e)
        return Response({'status':404,'message':"Invalid id"})
    
@api_view(['GET'])    
def getBooks(request):
    book = Book.objects.all() 
    serializers = BookSerializer(book, many=True)
    return Response({"status":200,"Data":serializers.data,"message":"Books get succeed"})
    
@api_view(['POST'])    
def addBooks(request):
    serializer = BookSerializer(data = request.data)
    if not serializer.is_valid():
         return Response({'status':403,'errors':serializer.errors,'message':"Something went wrong!"})
    serializer.save()
    return Response({'status':200,'payload':serializer.data,'message':"code Post success"})

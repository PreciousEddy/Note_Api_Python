
from django.shortcuts import render
from rest_framework.response import Response
from .models import Notes
from .serializers import NotesSerializer, RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

@api_view(['GET', 'POST'])
def notes_list(request, format=None):

    if request.method == 'GET':
        
        # get all of the notes / get the list of notes
        notes = Notes.objects.all()
        
        serializer = NotesSerializer(notes, many=True)
        
        return Response(serializer.data)



    if request.method == 'POST':
        
        serializer = NotesSerializer(data=request.data)
    
        if serializer.is_valid():
        
            serializer.save()
        
            return Response(serializer.data)
        

        
         
@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, pk, format=None):
    
    try:
        
        note_detail = Notes.objects.get(id=pk)
        
    except Notes.DoesNotExist():
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = NotesSerializer(note_detail)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT': 
     
        serializer = NotesSerializer(note_detail, data=request.data)
    
        if serializer.is_valid():
        
            serializer.save()
        
            return Response(serializer.data)
    
    
    
    
    elif request.method == 'DELETE':
        
        note_detail.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
@swagger_auto_schema(request_body=RegistrationSerializer)
def post(self, request, *args, **kwargs):
    context = {}
    
@api_view(['POST'])
def register(request):
    
    if request.method == 'POST':
        
        serializer = RegistrationSerializer(data=request.data)
        
        
        data = {}
        
        if serializer.is_valid():
            
            user = serializer.save()
            
            data['response'] = 'Success! Welcome new User'
            
            auth_token = Token.objects.get(user=user).key
            
            data['token'] = auth_token
            
        else:
            
            data = serializer.errors
            
        return Response(data)
    
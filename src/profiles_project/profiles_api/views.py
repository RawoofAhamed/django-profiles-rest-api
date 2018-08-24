from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'Uses HTTP methods as function(get,post,put,patch,delete)',
        'It is similar to traditional django views',
        'Gives most control over logics'
        'Is mannually mapped to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors,
             status=status.HTTP_4HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """Handles updating an object."""

        return Response({'method':'put'})


    def patch(self,request,pk=None):
        """Handles updating an fields provided in a request."""

        return Response({'method':'patch'})


    def delete(self, request, pk=None):
        """Deletes the record"""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
            serializer.errors, status= status.HTTP_400HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handles getting an object by id"""

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updating an object"""

        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handles updating part of an object."""

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handles deleting an object."""

        return Response({'http_method':'DELETE'})

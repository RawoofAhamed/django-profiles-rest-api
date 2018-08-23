from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self,request,format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'Uses HTTP methods as function(get,post,put,patch,delete)',
        'It is similar to traditional django views',
        'Gives most control over logics'
        'Is mannually mapped to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from .serializers import *
# Create your views here.
  
class VueViewSet(APIView):
    
    #serializer_class = VueSerializer
  
    def get(self, request):
        detail = {"message": 'Hello World!'} 
        return Response(detail)
  
    def post(self, request):
        pass

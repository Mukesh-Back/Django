from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import userseri
from .models import user
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

class View_User(APIView):
    
    def get(self,request):
        queryset=user.objects.all()
        serializer=userseri(queryset,many=True)
        return Response(serializer.data)


class UserListView(GenericAPIView):
    serializer_class=userseri()
    queryset=user.objects.all()
    def get(self,r): 
        serializer=self.serializer_class(self.get_queryset,many=True)
        return Response(serializer.data)



@api_view(["get"])
def vi(request):
    queryset=user.objects.all()
    serializer_class=userseri(queryset,many=True)
    return Response(serializer_class.data)

 




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ExampleAPIView(APIView):
    def get(self, request):
        print("")
        return Response( request.data,status=status.HTTP_200_OK)
   
from django.shortcuts import render
from .serializers import *
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response





# class IndustryApiView(APIView):
    
#     def get(self,request):
#         industry = Industry.objects.all()

#         serializer = InsdustrySerializers(industry, many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

######  Project List API  ########

class ProjectListApiView(APIView):

    def get(self,request):
        projects = Projects.objects.all()
        serializer = ProjectListSerializers(projects, context={'request':request}, many=True)

        response_data = {
            "status":"success",
            "message":"Data Retrive Successfully",
            "data":serializer.data
        }
        return Response(response_data)
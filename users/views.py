from django.shortcuts import render
from rest_framework import viewsets
from users.models import Company,Employee
from users.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.response import Response 
from rest_framework.decorators import action

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
      
    #companies/{companyID}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
          company = Company.objects.get(pk=pk)
          emps = Employee.objects.filter(company_id=company)
          emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
          return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'Company Does Not Exit Yet....!!!! ERROR COMPANY NOT FOUND'})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    
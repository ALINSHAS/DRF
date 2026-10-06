

from myapp.models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response

from myapp.serializers import EmployeeSerializer

#API view for reading all employee records

class EmployeeList( APIView):
    def get(self, request):
        e = Employee.objects.all()
        #read all employee records from employee table(qs)
        serializer_instance=EmployeeSerializer(e,many=True)
        #EmployeeSerializer converts qs into python native types
        #qs contains more than one record so we use many=True
        return Response(data=serializer_instance.data) 
        #sends python native data as json using Response class



#API view for creating a new employee record
class EmployeeCreate(APIView):
    def post(self, request):
       #view receives data as request.data(client side data-python native)
       #calls serializer class for deserialization.here we pass request.data as argument
       #after validation serializer saves data as model object inside db table
        serializer_instance=EmployeeSerializer(data=request.data)    # its written (data=) so its deserialization
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data) # used to get and see the added data
        #or
            # return Response({"message":"created"}) 
        else:
           return Response(serializer_instance.errors)



# API view for reading a specific employee
# from django.shortcuts import get_object_or_404
class EmployeeDetails(APIView):
    def get(self, request, i):
        e = Employee.objects.get(id=i)  #reads employee object from model
        # or
        # e=get_object_or_404(Employee,id=i)  # it is used instead of above line. if any error occurs or not valid data it will show 404 instead of another error
        serializer_instance=EmployeeSerializer(e) #converts model object into python native using EmployeeSerializer
        return Response(serializer_instance.data)  #sends the response as json



#API view for deleting a specific employee

from django.shortcuts import get_object_or_404

class EmployeeDelete(APIView):
    def delete(self,request,i):
        # e=Employee.objects.get(id=i)
        e=get_object_or_404(Employee,id=i)
        e.delete()
        return Response({"Message":"Deleted Successfully"})




#API view for full update

class Employeefullupdate(APIView):
    def put(self, request, i):
        e=Employee.objects.get(id=i)
        # or
        # e=get_object_or_404(Employee,id=i)
        serializer_instance=EmployeeSerializer(e,request.data)    
        if serializer_instance.is_valid():
            serializer_instance.save()   #calls update() inside serializer data
            return Response(serializer_instance.data) 
        else:
            return Response(serializer_instance.errors)
        


#API view for partial update

class Employeepartialupdate(APIView):
    def patch(self, request, i):
        e=Employee.objects.get(id=i)
        # or
        # e=get_object_or_404(Employee,id=i)
        serializer_instance=EmployeeSerializer(e,request.data,partial=True)    
        if serializer_instance.is_valid():
            serializer_instance.save()   #calls update() inside serializer data
            return Response(serializer_instance.data) 
        else:
            return Response(serializer_instance.errors)
                
        
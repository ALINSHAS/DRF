
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.models import Movie
from movies.serializers import MovieSerializer


#API view for reading all movie records
class MovieList( APIView):
    def get(self, request):
        m= Movie.objects.all()
        serializer_instance=MovieSerializer(m,many=True)
        return Response(serializer_instance.data) 


#API view for creating a new movie record
class MovieCreate(APIView):
    def post(self, request):
        serializer_instance=MovieSerializer(data=request.data)   
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data) 
        else:
           return Response(serializer_instance.errors)
        

#API View for reading all movie records and for creating a new movie record
#all the below codes  2 methods are done in one code
from rest_framework import status
class MovieListCreate(APIView):
    def get(self, request):
        m= Movie.objects.all()
        serializer_instance=MovieSerializer(m,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK) 
    def post(self, request):
            serializer_instance=MovieSerializer(data=request.data)   
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(serializer_instance.data,status=status.HTTP_201_CREATED) 
            else:
               return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


            
class MovieRetrievalUpdateDelete(APIView):

    # API view for retrieving one movie
    def get(self, request, i):
        m = Movie.objects.get(id=i)
        serializer_instance = MovieSerializer(m)
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)


    # API view for deleting one movie
    def delete(self, request, i):
        m = Movie.objects.get(id=i)
        m.delete()
        return Response({"Message": "Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)


    # API view for full update
    def put(self, request, i):
        m = Movie.objects.get(id=i)
        serializer_instance = MovieSerializer(m,data=request.data)
        if serializer_instance.is_valid():

            # Data after validation
            # cleaned_data=serializer_instance.validated_data
            # title=cleaned_data['title']

            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



    # API view for partial update
    def patch(self, request, i):
            m=Movie.objects.get(id=i)
            serializer_instance=MovieSerializer(m,data=request.data,partial=True)    
            if serializer_instance.is_valid():
                serializer_instance.save()  
                return Response(serializer_instance.data,status=status.HTTP_201_CREATED) 
            else:
                return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
                        
                        
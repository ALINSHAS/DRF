from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movies.serializers import UserSerializer



class MovieView(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
   


# #Search API view
from django.db.models import Q
class SearchAPIView(APIView):
    def get(self,request):

        #fetches data coming from request url
        data = request.query_params.get('search')   

        #filters movie records having title matching with data
        m=Movie.objects.filter(Q(title__icontains=data)| 
                               Q(director__icontains=data)| 
                               Q(language__icontains=data))
        if not m.exists():
            return Response({"Message":"No Records Found"},status=status.HTTP_200_OK)
        
        #coverts the qs into native type using serializer class
        serializer_instance=MovieSerializer(m,many=True)

        #returns response as json using Response class
        return Response(serializer_instance.data,status=status.HTTP_200_OK)




# above code using generics
from rest_framework import generics
from rest_framework.filters import SearchFilter
class SearchAPIView(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backends=[SearchFilter]
    search_fields=['title','director','language']


class RegisterAPIView(APIView):
    def post(self, request):
        serializer_instance=UserSerializer(data=request.data)   
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED) 
        else:
           return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
                        
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework import generics


class MovieListCreate(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
   


class MovieRetrievalUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    

  



                        
                        
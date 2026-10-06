
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework import mixins,generics


class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
            return self.create(request)



            
class MovieRetrievalUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    def get(self,request,pk):
            return self.retrieve(request,pk)
    def put(self,request,pk):
            return self.update(request,pk)
    def patch(self,request,pk):
            return self.partial_update(request,pk)
    def delete(self,request,pk):
            return self.destroy(request,pk)

  



                        
                        
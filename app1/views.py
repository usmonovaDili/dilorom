from django.shortcuts import render
from rest_framework import generics, mixins, status
from .models import Books
from .serializers import BooksSerializer


# Create your views here.


class BooksApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.retrieve(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

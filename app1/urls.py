from django.urls import path
from .views import BooksApiView

urlpatterns = [
    path('',BooksApiView.as_view()),
]


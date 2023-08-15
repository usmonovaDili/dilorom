from django.urls import path
from .views import APIBookDetailView,APIBookListView,BookListByAuthorView

urlpatterns = [
    path('', APIBookListView.as_view()),
    path('books/<int:pk>/', APIBookDetailView.as_view()),
    path('authors/<int:author_id>/books/', BookListByAuthorView.as_view()),

]

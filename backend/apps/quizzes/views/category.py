from rest_framework import generics
from ..models import Category, Quiz, Question, Option
from ..serializers import CategorySerializer, QuizSerializer, QuestionSerializer, OptionSerializer



class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        queryset = Category.objects.order_by('name')
        return queryset
    
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

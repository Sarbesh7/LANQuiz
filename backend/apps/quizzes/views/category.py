from rest_framework import generics
from ..models import Category, Quiz, Question, Option
from ..serializers import CategorySerializer, QuizSerializer, QuestionSerializer, OptionSerializer



class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.order_by('name')
    serializer_class = CategorySerializer
    
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.order_by('name')
    serializer_class = CategorySerializer
    lookup_field = 'pk'

from rest_framework import generics
from ..models import Category, Quiz, Question, Option
from ..serializers import CategorySerializer, QuizSerializer, QuestionSerializer, OptionSerializer



class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.order_by('created_at')
    serializer_class = QuizSerializer

class QuizRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.order_by('created_at')
    serializer_class = QuizSerializer
    lookup_field = 'pk'



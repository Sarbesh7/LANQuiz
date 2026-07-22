from rest_framework import generics
from ..models import Category, Quiz, Question, Option
from ..serializers import CategorySerializer, QuizSerializer, QuestionSerializer, OptionSerializer





class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.order_by('order')
    serializer_class = QuestionSerializer

class QuestionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.order_by('order')
    serializer_class = QuestionSerializer
    lookup_field = 'pk'



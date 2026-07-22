from rest_framework import generics
from ..models import Category, Quiz, Question, Option
from ..serializers import CategorySerializer, QuizSerializer, QuestionSerializer, OptionSerializer


class OptionListCreateView(generics.ListCreateAPIView):
    queryset = Option.objects.order_by('order')
    serializer_class = OptionSerializer

class OptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.order_by('order')
    serializer_class = OptionSerializer
    lookup_field = 'pk'


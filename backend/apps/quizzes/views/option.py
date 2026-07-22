from rest_framework import generics
from ..models import Category, Quiz, Question, Option
from ..serializers import CategorySerializer, QuizSerializer, QuestionSerializer, OptionSerializer


class OptionListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Option.objects.order_by('order')
        return queryset
    
    serializer_class = OptionSerializer

class OptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    lookup_field = 'pk'


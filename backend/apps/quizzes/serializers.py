from .models import Category, Quiz, Question, Option
from rest_framework import serializers
from apps.common.base import BaseModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class  OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"



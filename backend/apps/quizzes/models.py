import uuid
from django.db import models
from apps.common.base import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]


class Quiz(BaseModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='quizzes'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_per_question = models.PositiveSmallIntegerField(default=20)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"


class Question(BaseModel):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    text = models.TextField()
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["quiz", "order"],
                name="unique_question_order_per_quiz",
            )
        ]

    def __str__(self):
        return f"{self.quiz.title} - {self.text[:30]}"


class Option(BaseModel):
    question = models.ForeignKey(
        Question,  
        on_delete=models.CASCADE,
        related_name="options",
    )
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["question", "order"],
                name="unique_option_order_per_question",
            )
        ]

    def __str__(self):
        return f"{self.question.text[:30]} - {self.text}"
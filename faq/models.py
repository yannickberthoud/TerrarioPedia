from django.db import models
from card.models import Category


class Faq(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=512)
    answer = models.TextField()

    def __self__(self):
        return self.question

from django.db import models
from django.contrib.auth.models import User
from random import choice
from datetime import datetime
from problems.models import Problem


def simple():
    return {"1 2": "2"}

def slugify():
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    date = str(datetime.now()).replace(" ", "")
    date = date.replace(":", "")
    date = date.replace(".", "")
    date = date.replace("-", "")
    slug = ""
    for i in range(5):
        slug += choice(uppers)
        slug += choice(lowers)
        slug += choice(digits)
        slug += choice(date) 
    return slug

class Attempt(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Urinish muallifi", related_name="attempt_author")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="attempt_problem", verbose_name="Urinish masalasi")
    slug = models.CharField(max_length=30, default=slugify, editable=False, unique=True, verbose_name="Urinish slugi")
    language = models.CharField(max_length=20, verbose_name="Urinish tili")
    code = models.TextField(null=True, blank=True, default="", verbose_name="Urinish dasturi")
    cases = models.JSONField(default=simple, null=True, blank=True)
    status = models.CharField(max_length=200)
    codelength = models.IntegerField(default=0, verbose_name="Urinish kod uzunligi")
    time = models.FloatField(default=0, verbose_name="Urinish vaqti")
    memory = models.FloatField(default=0, verbose_name="Urinish xotirasi")
    error = models.TextField(default="", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    buyers = models.ManyToManyField(User, related_name="attempt_buyers")

    def save(self, *args, **kwargs):
        self.codelength = len(self.code)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.status
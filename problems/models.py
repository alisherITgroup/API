from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from random import choice
from datetime import datetime

STATUS = (
    ("easy", "Easy"),
    ("medium", "Medium"),
    ("hard", "Hard")
)

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
    return slug.replace(slug[-1], "p")

class Language(models.Model):
    command = models.CharField(max_length=200, verbose_name="Til uchun buyruqlar")
    name = models.CharField(max_length=100, verbose_name="Til")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tag")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Problem(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="problem_author")
    slug = models.CharField(max_length=30, default=slugify, editable=False, unique=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Masala nomi")
    problem = models.TextField(verbose_name="Masala matni")
    timelimit = models.IntegerField(verbose_name="Masala vaqt chegarasi", default=1000)
    memorylimit = models.IntegerField(verbose_name="Masala xotira chegarasi", default=16)
    difficulty = models.IntegerField(verbose_name="Masala qiyinchiligi")
    price = models.IntegerField(verbose_name="Masala narxi")
    type = models.CharField(max_length=20, choices=STATUS)
    tags = models.ManyToManyField(Tag, related_name="problem_tags")
    infoin = models.TextField(null=True, blank=True, verbose_name="Masala kirish ma'lumotlari")
    infoout = models.TextField(null=True, blank=True, verbose_name="Masala chiqish ma'lumotlari")
    comment = models.TextField(null=True, blank=True, verbose_name="Masala uchun izox")
    simpletests = models.JSONField(default=simple, null=True, blank=True, verbose_name="Masala simpletestlari")
    tests = models.JSONField(default=simple, null=True, blank=True, verbose_name="Masala testlari")
    is_interactive = models.BooleanField(default=False, verbose_name="Interactive/Non interactive")
    solution = models.TextField(null=True, blank=True, verbose_name="Masala yechimi")
    solvers = models.ManyToManyField(User, related_name="problem_solvers")
    errors = models.ManyToManyField(User, related_name="problem_errors")
    likes = models.ManyToManyField(User, related_name="problem_likes")
    unlikes = models.ManyToManyField(User, related_name="problem_unlikes")
    buyers = models.ManyToManyField(User, related_name="problem_buyers", verbose_name="Masalani yechimini sotib olganlar")
    casebuyers = models.ManyToManyField(User, related_name="problem_casebuyers", verbose_name="Masalani testcaselarini sotib olganlar")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def count(self):
        return Problem.objects.all().count()
    
    def count_likes(self):
        return self.likes.count()
    def count_unlikes(self):
        return self.unlikes.count()
    def count_buyers(self):
        return self.buyers.count()
    def count_casebuyers(self):
        return self.casebuyers.count()
    def count_solvers(self):
        return self.solvers.count()
    def count_errors(self):
        return self.errors.count()

class Comment(models.Model):
    reply_id = models.IntegerField(default=0, null=True, blank=True, verbose_name="Izox reply")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="problem_comment_author", verbose_name="Izox muallifi")
    body = models.TextField(verbose_name="Izox matni")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
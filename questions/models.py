from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class Question(models.Model):
    date = models.DateField()
    subject = models.CharField(max_length=10)
    number = models.IntegerField(default=0)
    question_text = models.TextField()
    tags = models.ManyToManyField(Tag)
    notes = models.TextField(default='', blank=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date} {self.subject} #{self.number}'

    def desc(self):
        return self.question_text[:20]
from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Question, Tag
from django.db.models import Max, Q
import random

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'questions/detail.html'

class TagView(generic.ListView):
    model = Tag
    template_name = 'questions/tag.html'

    context_object_name = 'questions_with_tag'
    def get_queryset(self):
        pk = self.kwargs['pk']
        instance = Tag.objects.get(pk=pk)
        name = instance.name
        return (name, Question.objects.filter(tags__id=pk).order_by('-date'))

class TagListView(generic.ListView):
    model = Tag
    template_name = 'questions/tag_list.html'

    context_object_name = 'tags'
    def get_queryset(self):
        return Tag.objects.order_by('name')

class RandomView(generic.ListView):
    model = Question
    template_name = 'questions/random.html'
    context_object_name = 'random_question'

    def get_queryset(self):
        max_id = Question.objects.all().aggregate(max_id=Max('id'))['max_id']

        while True:
            pk = random.randint(1, max_id)
            question = Question.objects.filter(pk=pk).first()
            if question:
                return question

class SearchResultsView(generic.ListView):
    model = Question
    template_name = 'questions/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        question_list = Question.objects.filter(
            Q(subject__icontains=query) | Q(question_text__icontains=query))
        return question_list
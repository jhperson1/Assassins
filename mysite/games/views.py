# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import People, KillFeed

def index(request):
    context = {}
    return render(request, 'games/index.html', context)

def players(request):
    return HttpResponse("not yet implemented")

def killfeed(request):
    return HttpResponse("not yet implemented")

def you(request, name):
    return HttpResponse("not yet implemented")

def join(request):
    return HttpResponse("not yet implemented")

def login(request):
    return HttpResponse("not yet implemented")

def profile(request, name):
    return HttpResponse("not yet implemented")

def submit_a_kill(request):
    return HttpResponse("not yet implemented")

def status(request, name):
    return HttpResponse("not yet implemented")

# def detail(request, question_id):
#     # # dynamic nonshortcut
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})
#     # Shortcut
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
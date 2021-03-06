from django.http.response import Http404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Questions,Choice
# Create your views here.


def index(request):
    latest_question_list = Questions.objects.all()
    context = {'latest_question_list':latest_question_list}
    return render(request,'Gym/index.html',context)

def detail(request, question_id):
  try:
    question = Questions.objects.get(pk=question_id)
  except Questions.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'Gym/detail.html', { 'question': question })

def summary(request, question_id):
  question = get_object_or_404(Questions, pk=question_id)
  return render(request, 'Gym/summary.html', { 'question': question })


def record(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Gym/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.days += 1
        selected_choice.save()
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Gym:summary', args=(question.id,)))
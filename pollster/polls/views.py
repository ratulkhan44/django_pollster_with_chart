from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse


# Create your views here.

def index(request):
    questions = Question.objects.order_by('pub_date')[:5]
    context = {
        'questions': questions,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Doesn't exist")

    context = {
        'question': question
    }

    return render(request, 'polls/details.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': 'You didn\'t select a choice'
        }
        return render(request, 'polls/details.html', context)

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results_data(request, question_id):
    vote_data = []
    question = Question.objects.get(pk=question_id)
    votes = question.choice_set.all()

    for vote in votes:
        vote_data.append({vote.choice_text: vote.votes})

    return JsonResponse(vote_data, safe=False)

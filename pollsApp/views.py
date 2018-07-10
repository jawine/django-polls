from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    # retrieve list of questions from Question model
    # retrieve up to 5
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'pollsApp/index.html', context)

def detail(request, question_id):
    """Can use try catch block
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 
        'pollsApp/detail.html',
        {'question': question})
    """
    # or use get_object_or_404 shortcut
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 
        'pollsApp/detail.html',
        {'question': question})


def results(request, question_id):
    response = "Viewing results of question %s." 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s." %
        question_id)
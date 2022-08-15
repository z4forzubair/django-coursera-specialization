from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from polls.models import Question


def index(request):
    latest_question_list = get_list_or_404(Question)
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("Results for question: %s" % question_id)


def vote(request, question_id):
    return HttpResponse("VOte for question: %s" % question_id)


def owner(request):
    return HttpResponse("Hello, world. 1d5e229a is the polls index.")

from django.shortcuts import render
from django.http import HttpResponse, response
from .models import Question

# Create your views here.
# def index(request):
#     response = HttpResponse()
#     response.writelines("<h1>Xin chào</h1>")
#     response.write("Đây là app polls")
#     return response
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    print(request.GET)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output) 

def test_view(request):
    return 'Hello internet'

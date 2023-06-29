from django.shortcuts import render
# from django.http import HttpResponse #삭제
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # DB에 없는 ID를 url에 입력하여 500 Error발생시 그 에러를 404로 바꿔주는 것
    #get_object_or_404(객체, pk값) -> 객체 return
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # set질문자의 답변(textarea의 name으로 전달받은 value값)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question_id)

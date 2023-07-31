from django.shortcuts import render
# from django.http import HttpResponse #삭제
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
# from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    page = request.GET.get('page', 1) #페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) #question_list를 페이지당 10개씩
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}  # question_list는 페이징 객체(page_obj)
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # DB에 없는 ID를 url에 입력하여 500 Error발생시 그 에러를 404로 바꿔주는 것
    #get_object_or_404(객체, pk값) -> 객체 return
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url="common:login")
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user #author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url="common:login")
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

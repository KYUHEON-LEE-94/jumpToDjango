from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

def index(request):
    page = request.GET.get('page', 1) #페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) #question_list를 페이지당 10개씩
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}  # question_list는 페이징 객체(page_obj)
    return render(request, 'pybo/question_list.html', context)


 #question_id를 request로 받음
def detail(request, question_id):
    # DB에 없는 ID를 url에 입력하여 500 Error발생시 그 에러를 404로 바꿔주는 것
    #get_object_or_404(객체, pk값) -> 객체 return
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
from django.http import HttpResponse, Http404  # html파일 없이 결과값 출력해주는 패키지 
from .models import *
from django.shortcuts import render
from django.shortcuts import render, get_list_or_404

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = '   ,   '.join([q.question_text for q in latest_question_list])
    #context = { 'question_list': [] }
    context = {'question_list': latest_question_list}
    return render(request, 'index.html', context)

def detail (request, question_id):
    '''
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('당신이 찾는 페이지는 없어요')
    '''
    q = get_list_or_404(Question, pk=question_id)

    context = {'question': q}
    
    return render(request, 'detail.html', context)

def some_url(request):
    return HttpResponse('썸 URL 구현해보기 성공!')

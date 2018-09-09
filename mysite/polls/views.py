from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, wolrd! You're at the polls index.")

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # queryset = Question.objects.all()

    # get_queryset默认为Model.objects.all()
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # value="{{ choice.id }}
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 找不到：重新渲染投票表单
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message': "你没有进行选择"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 用redirect，因为防止用户按“返回键”，将表单提交两次。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))



from django.urls import path
from . import views

# add an app_name to set the application namespace, 在模板中{% url 'polls:detail' question.id %}
app_name = 'polls'

urlpatterns = [
    # ex: /polls
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/results/1
    path('results/<int:pk>/', views.ResultView.as_view(), name='results'),
    # ex: /polls/vote/1
    path('vote/<int:question_id>/', views.vote, name='vote'),
]
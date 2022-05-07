from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latestQuestionList'
    
    def get_queryset(self):
        ''' Return the last five published questions (not including those set to be 
        published in the future).'''
        return Question.objects.filter(pubDate__lte=timezone.now()).order_by('-pubDate')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
class ResultsView(generic.DetailView):
    model =  Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selectedChoice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selectedChoice.votes += 1
        selectedChoice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
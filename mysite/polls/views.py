#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

def index(request):
	latest_question_list = Question.objects.order_by('-pub_data')[:5]
	#output = ', '.join([p.question_text for p in latest_question_list])
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
	#return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
	#response = "You're looking at question %s."
	#return HttpResponse(response % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

	#return HttpResponse("You are voting on question %s." % question_id)

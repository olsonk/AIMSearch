from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import auth
from django.core.context_processors import csrf
import datetime

from search.models import Standard, Issue, Activity

# Create your views here.
def index(request):
	issues = Issue.objects.all()
	return render_to_response('search/index.html', 
								{'issues': issues,
								})
	
def grade(request, grade):
	model = Standard
	if grade != 0:
		standards = Standard.objects.filter(code__startswith=grade)
	elif grade == 0:
		standards = Standard.objects.filter(code__startswith=K)
	return render(request, 'search/grade.html', {
					'standards': standards,
					})
					
class StandardDetail(generic.DetailView):
	model = Standard
	template_name = "search/standard.html"
	
def issue(request, issue):
	current_issue = Issue.objects.get(pk=issue)
	issue_activities = Activity.objects.filter(issue__id=issue)
	return render(request, "search/issue.html", {'activities': issue_activities,
													'issue': current_issue})
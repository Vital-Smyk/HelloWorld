from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

def get_projects(request,*args,**kwargs):
    projects = Project.objects.all().values()
    context = {
        'projects' : list (projects),
    }
    # return HttpResponse(content=projects)
    return render(
        request = request,
        template_name = './all_projects.html',
        context = context,
    )


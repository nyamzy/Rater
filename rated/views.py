from django.shortcuts import render, redirect
from rated.models import Projects, Profile

# Create your views here.
def index(request):
    title = "Welcome to Reviewer"
    projects = Projects.objects.all().order_by('-id')

    context = {
        "title": title,
        "projects": projects,
    }
    
    return render(request, "all-rated/index.html", context)

def search(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get("project")
        searched_projects = Projects.search_project(search_term)
        message = f"{search_term}"

        return render(request, 'all-rated/search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-rated/search.html', {"message": message})
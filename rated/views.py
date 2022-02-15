from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from rated.models import Projects, Profile, Rating
from django.contrib.auth.decorators import login_required
from .forms import PostProjectForm, CreateProfileForm

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

@login_required(login_url='/accounts/login/')
def project(request, project_id):
    try:
        project = Projects.objects.get(id = project_id)
    except Projects.DoesNotExist:
        raise Http404()
    return render(request, "all-rated/project.html", {"project": project})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.user = current_user
            project.save()
        return redirect('index')

    else:
        form = PostProjectForm()
    return render(request, "new_project.html", {"form": form})


@login_required(login_url='/accounts/login/')
def rate(request, id):
    if request.method == 'POST':
        project = Projects.objects.get(id = id)
        current_user = request.user
        design_rate = request.POST['design']
        usability_rate = request.POST['usability']
        content_rate = request.POST['content']

        Rating.objects.create(
            project = project,
            user = current_user,
            design_rating = design_rate,
            usability_rating = usability_rate,
            content_rating = content_rate,
            average = round((float(design_rate) + float(usability_rate) + float(content_rate)) / 3,1)
        )
        rating = Rating.objects.filter(project = project)

        return render(request, "all-rated/project.html", {"project":project, "rating": rating})
    else:
        project = Projects.objects.get(id = id)
        return render(request, "all-rated/project.html", {"project": project, "rating": rating})


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = CreateProfileForm()
    return render(request, "profile/create_profile.html", {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id = current_user.id).first()
    project = Projects.objects.filter(user_id = current_user.id)

    return render(request, "profile/profile.html", {"profile": profile, "project": project})


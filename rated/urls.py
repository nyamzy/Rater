from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search/', views.search, name='search_results'),
    path('project/<int:project_id>', views.project, name = 'project'),
    path('new/project/', views.new_project, name = 'new-project'),
    path('rate/<int:id>', views.rate, name = 'rate'),
    path('profile/', views.profile, name = "profile"),
    path('profile/create/', views.create_profile, name = 'create-profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
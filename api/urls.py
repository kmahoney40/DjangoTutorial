from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, CreateTempView, CreateRunTimesView, DetailsRunTimesView


urlpatterns = [
    re_path(r'^bucketlists/$', CreateView.as_view(), name="create"),
    re_path(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    re_path(r'^temp/$', CreateTempView.as_view(), name="createtemp"),
    # For testing only (load the test database), the actual app will not create the table 
    # or any rows
    re_path(r'^runtimes/$', CreateRunTimesView.as_view(), name="createruntimes"),
    re_path(r'^save/(?P<pk>[0-9]+)$', DetailsRunTimesView.as_view(), name="detailsruntimes"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

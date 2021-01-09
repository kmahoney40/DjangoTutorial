from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, CreateTempView, CreateRunTimesView


urlpatterns = [
    re_path(r'^bucketlists/$', CreateView.as_view(), name="create"),
    re_path(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    re_path(r'^temp/$', CreateTempView.as_view(), name="createtemp"),
    re_path(r'^runtimes/$', CreateRunTimesView.as_view(), name="createruntimes"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

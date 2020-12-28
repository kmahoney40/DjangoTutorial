from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.db import transaction
from .models import RunTimes

class IndexView(generic.ListView):
    #model = RunTimes
    template_name = 'water/index.html'
    #context_object_name = 'run_time'
    
    def get_queryset(self):
        return HttpResponse("WOOT")


class RuntimeView(generic.ListView):
    #model = RunTimes
    template_name = 'water/runtime.html'
    context_object_name = 'run_time_list'
    
    def get_queryset(self):
        return RunTimes.objects.order_by('day')


class EditView(generic.DetailView):
    model = RunTimes
    template_name = 'water/edit.html'

    def get_queryset(self):
        return RunTimes.objects.filter(id=self.kwargs['pk'])

def save(request):
    runtimes = RunTimes.objects.order_by('day')
    #todo  days had better be 8 add error checking - 8 days plus id = 8, day = 7 for manual.
    days = runtimes.count()
    for day in range(days):
        run = get_object_or_404(RunTimes, day=day)
        name = 'day' + str(day)
        run.v1 = request.POST.get(name+'v1')
        run.v2 = request.POST.get(name+'v2')
        run.v3 = request.POST.get(name+'v3')
        run.v4 = request.POST.get(name+'v4')
        run.v6 = request.POST.get(name+'v5')
        run.v6 = request.POST.get(name+'v6')
        run.v7 = request.POST.get(name+'v7')
        run.save()

    return HttpResponseRedirect(reverse('water:runtime'))
    
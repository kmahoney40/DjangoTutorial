from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.db import transaction
from .models import RunTimes
from .models import Manual

class IndexView(generic.ListView):
    #model = RunTimes
    template_name = 'water/index.html'
    #context_object_name = 'run_time'
    
    def get_queryset(self):
        return HttpResponse("WOOT")

class ManualView(generic.ListView):
    template_name = 'water/runtime.html'
    context_object_name = 'manual_list'
    
    def get_queryset(self):
        return Manual.objects.order_by('id')

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
    #todo  days had better be 8 add error checking - 7 days plus id = 8, day = 7 for manual.
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
    
def manual(request):
    manual = get_object_or_404(Manual, id=1)
    manual.m1 = request.POST.get('v1')
    manual.m2 = request.POST.get('v2')
    manual.m3 = request.POST.get('v3')
    manual.m4 = request.POST.get('v4')
    manual.m5 = request.POST.get('v5')
    manual.m6 = request.POST.get('v6')
    manual.m7 = request.POST.get('v7')
    manual.save()
    
    return HttpResponseRedirect(reverse('water:runtime'))
    
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

    
def save(request, runtimes_id):
    
    
    
    runtimes = get_object_or_404(RunTimes, pk=runtimes_id)
    
    # this gets the table (a row from the table) from the database. 
    # The table has not been updated, the form has not been saves. We
    # need to push the form into the table.
    #rt = get_object_or_404(RunTimes, pk=runtimes_id)
    runtimes.v1 = request.POST.get('v1')
    runtimes.v2 = request.POST.get('v2')
    runtimes.v3 = request.POST.get('v3')
    runtimes.v4 = request.POST.get('v4')
    runtimes.v5 = request.POST.get('v5')
    runtimes.v6 = request.POST.get('v6')
    runtimes.v7 = request.POST.get('v7')
    runtimes.save(update_fields=['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7'])
    
    #transaction.commit()
    #return RunTimes.objects.all().order_by('day')
    #RunTimes.save()
    return HttpResponseRedirect(reverse('water:runtime'))

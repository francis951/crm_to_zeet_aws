from django.shortcuts import render, redirect
from .forms import GENQModelsForm
from .models import GENQModels
from django.contrib import messages
# Create your views here.
#read data
def data_read(request):
    customer = GENQModels.objects.all()
    return render(request, 'Data_output.html', {'customer':customer})
#post data
def form_data(request, id =None):
    form = GENQModelsForm()
    if request.method == 'POST':
        form = GENQModelsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/data')
    return render(request, 'form_data.html', {'form': form}) 

#delete
def data_delete(request, candidate_id):
    candidate = GENQModels.objects.get(id = candidate_id)
    candidate.delete()
    return redirect('/data')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import New_project
from .forms import New_projectForm
from django.views.generic import DetailView, UpdateView, DeleteView
def index(request):
    data = New_project.objects.all()
    news = {
        'news':data
    }
    return render(request, 'main/index.html', news)
def about(request):
    main_id = {'true_fact':'F**K qwasar.io'}
    return render(request, 'main/about.html', main_id)


class NewDetailView(DetailView):
    model = New_project
    template_name = 'main/new_details.html'
    context_object_name = 'converter'

class NewUpdateView(UpdateView):
    model = New_project
    template_name = 'main/create.html'

    fields = ['file_name', 'file_size', 'some_info']

class NewDeleteView(DeleteView):
    model = New_project
    success_url = '/'
    template_name = 'main/delete_detail.html'

def create(request):

    error = ''
    if request.method == 'POST':
        error = ''
        form = New_projectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            error = 'Inputs are invalid'

    form = New_projectForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/create.html', data)



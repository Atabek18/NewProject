from django.shortcuts import render
from django.http import HttpResponse
def index(request):

    return render(request, 'main/index.html')
def about(request):
    main_id = {'true_fact':'F**K qwasar.io'}
    return render(request, 'main/about.html', main_id)



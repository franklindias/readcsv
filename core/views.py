from django.shortcuts import render
import csv
import os

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def read(request):
    
    reader = csv.reader(open(os.path.abspath(request.POST['csv']),"rt"), delimiter=';')
    
    for row in reader:

        print(row[3])


    
    return render(request, 'index.html', {'doc':reader})
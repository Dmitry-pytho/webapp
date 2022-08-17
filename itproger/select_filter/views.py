from django.shortcuts import render

# Create your views here.

def select_filter(request):
    return render(request, 'select_filter/select_filter.html')
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'cv_builder_app/index.html') 

def about(request):
    return render(request, 'cv_builder_app/about.html') 
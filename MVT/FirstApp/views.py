from django.shortcuts import render

# Create your views here.

def baseview(request):
    template_name='FirstApp/base.html'
    return render(request, template_name)
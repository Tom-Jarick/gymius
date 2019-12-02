from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def content(request):
    context={"content":"hello TOM"}
    return render(request,"workouts/content.html",context)


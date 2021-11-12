from django.shortcuts import render
from django.http.response import HttpResponse
from django import forms

tasks=["Diska","Göra läxor", "plugga webb"]
class NewTaskForm(forms.Form):
    task=forms.CharField(label="Add task")
# Create your views here.
def tasklist(request):
    return render(request, 'index.html')
def add(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasks.append(task)
            return render(request,"add.html",{ 
                'tasklist':tasks,
                'form':form
            })
    else:
        return render(request,"add.html", {
            "form":NewTaskForm(),
            "tasklist":tasks
        })
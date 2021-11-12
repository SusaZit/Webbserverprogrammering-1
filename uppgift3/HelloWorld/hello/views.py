from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def leo(request):
    return HttpResponse("<h1>hej Leo!</h1>")      
def hello(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def news(request):
    return render(request, 'news.html')
def contact(request):
    return render(request, 'contact.html')
def greet(request, name):
    return render(request, "index.html",{"lista" : ['banan', 'apelsin', 'apple', 'godis', 'läsk'], "name":name})
 
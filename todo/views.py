from django.shortcuts import render

def say_hello(request):
    return HttpResponse("todo/todo_list.html")

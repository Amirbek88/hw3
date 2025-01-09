from django.shortcuts import render

# Создайте ваши представления здесь.

def index(request):
    return render(request, 'index.html') 

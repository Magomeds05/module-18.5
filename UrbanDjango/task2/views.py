import django
from django.shortcuts import render
from django.views.generic import TemplateView

def func_task2(request):
    return render(request, 'second_task/func_template.html')

class ViewByClass(TemplateView):
    template_name = 'second_task/func_template.html'

# Create your views here.
# В представлениях (views) приложения task2 создайте представления:
# одно классовое, а другое функциональное, которые отображают шаблоны с соответствующими надписями.
# Названия для представлений можете определить самостоятельно.
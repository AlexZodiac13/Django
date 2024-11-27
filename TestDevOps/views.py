# mainapp/views.py
from django.shortcuts import render
from .tasks import add


def home(request):
    # Запускаем задачу Celery и ожидаем результат
    result = add.delay(4, 4)
    result_value = result.get()  # Ждем завершения задачи и получаем результат
    
    # Передаем результат в шаблон
    return render(request, 'index.html', {'result': result_value})

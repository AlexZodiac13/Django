from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# устанавливаем модуль settings Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestDevOps.settings')

# создаем экземпляр приложения Celery
app = Celery('TestDevOps')

# используем строку настроек Django как конфигурационный файл Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# автоматически находим задачи в приложениях
app.autodiscover_tasks()

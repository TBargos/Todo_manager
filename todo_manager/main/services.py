"""Обслуживающие функции для приложения main"""
from main.models import Task

def load_actual_tasks():
    """Загружает активные задачи"""
    return Task.objects.filter(status=True)

def load_completed_tasks():
    """Загружает завершённые задачи"""
    return Task.objects.filter(status=False)
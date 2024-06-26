"""Обслуживающие функции для приложения main"""
from django.shortcuts import get_object_or_404
from main.models import Task


def load_actual_tasks():
    """Загружает активные задачи"""
    return Task.objects.filter(status=True)

def load_completed_tasks():
    """Загружает завершённые задачи"""
    return Task.objects.filter(status=False)

def add_new_task(task: str) -> None:
    """Добавляет новую задачу"""
    if isinstance(task, str):
        Task.objects.create(taskname=task)

def mark_task_finished(task_id):
    """Убирает задачу в список завершённых"""
    task = get_object_or_404(Task, id=task_id)
    task.status = False
    task.save()
    
def del_finished_tasks():
    """Удаляет завершённые задачи из БД"""
    Task.objects.all().filter(status=False).delete()
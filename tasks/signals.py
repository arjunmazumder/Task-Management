from django.db.models.signals import m2m_changed
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings
from tasks.models import Task

@receiver(m2m_changed, sender=Task.assignedTo.through)
def notify_employees_on_task_creation(sender, instance, action, **kwargs):
  
    if action == "post_add":
        # Get only the employees who were newly assigned
        assigned_employees = instance.assignedTo.all()
        
        for emp in assigned_employees:

            send_mail(
                subject="NEW TASK ASSIGNED",
                message=f"Hi {emp.name}, you have been assigned to '{instance.title}'!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[emp.email],
                fail_silently=False,
            )

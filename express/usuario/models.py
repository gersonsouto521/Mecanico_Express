from django.db import models
 
class Task(models.Model):
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )
 
    title = models.CharField(max_length=255)
    servico = models.CharField(max_length=20)
    placa = models.CharField(max_length=8)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
 
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
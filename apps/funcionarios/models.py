from django.db import models

# Create your models here.

class Funcionarios(models.Model):
    models.CharField(max_length=100, help_text='Funcionarios')

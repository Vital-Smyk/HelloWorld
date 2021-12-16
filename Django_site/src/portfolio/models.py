from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name =  models.CharField(
        verbose_name='Имя проекта',
        help_text='Длина имени максимум 255 символов',
        max_length=255,
        )
    create_at = models.DateField(
        verbose_name = 'Дата создания проекта'
    )
    user = models.ForeignKey(
        to=User,
        on_delete = models.PROTECT, 
    )

    def __str__(self) -> str:
        return f'{self.name}'
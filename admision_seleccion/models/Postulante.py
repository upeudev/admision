# _*_ coding: utf-8 _*_
import uuid
from django.db import models
from .Modalidad import Modalidad


class Postulante(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    modalidad = models.ForeignKey(Modalidad, null=True, blank=True)

    class Meta:
        verbose_name = "Postulante"
        verbose_name_plural = "Postulantes"

    def __str__(self):
        return self.nombre

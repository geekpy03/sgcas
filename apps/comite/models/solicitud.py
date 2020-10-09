from django.db import models
from apps.usuario.models import User
from apps.item.models import Item
from apps.linea_base.models import LineaBase
from apps.proyecto.models import Proyecto

tipo_solicitud = [('Item', 'Item'), ('LineaBase', 'LineaBase')]

class Solicitud(models.Model):
	asunto = models.CharField(max_length=100, default="")
	solicitante = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='solicitante', blank=True, null=True)
	votantes = models.ManyToManyField(User, blank=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, blank=True, null=True)
	tipo = models.CharField(max_length=100, choices=tipo_solicitud, default='Item')
	linea_base = models.ForeignKey(LineaBase, on_delete=models.CASCADE, blank=True, null=True)  
	votacion = models.IntegerField(default=0)
	descripcion = models.TextField()

	def __str__(self):
		return self.asunto
from django.db import models

class Dados(models.Model):
    sensor = models.BooleanField(default=False)
    botao = models.BooleanField(default=False)
    liga_robo = models.BooleanField(default=False)
    reset_contador = models.BooleanField(default=False)
    valor_contagem = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dados {self.id}"

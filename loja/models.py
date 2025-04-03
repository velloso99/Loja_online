from django.db import models

class produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')
    link_externo = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.nome

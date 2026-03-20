from django.db import models
from django.utils import timezone

class CategoriaStaff(models.Model):
    nome = models.CharField(max_length=100)
    ordem_hierarquia = models.IntegerField(help_text="Ex: 1 para Alta Cúpula, 2 para Líderes, etc.")

    def __str__(self):
        return self.nome
    class Meta:
        ordering = ['ordem_hierarquia']

class MembroStaff(models.Model):
    nick = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaStaff, on_delete=models.CASCADE)
    cargo_especifico = models.CharField(max_length=100, blank=True, null=True)
    foto_boneco = models.ImageField(upload_to='staff_fotos/', default='default_skin.png')

    def __str__(self):
        return f"{self.nick} - {self.categoria.nome}"

class NoticiaJornal(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem_capa = models.ImageField(upload_to='jornal_fotos/', blank=True, null=True)
    data_publicacao = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=50, default="Administração")

    def __str__(self):
        return self.titulo
    class Meta:
        ordering = ['-data_publicacao']

class CalendarioGuerra(models.Model):
    DIAS_DA_SEMANA = [
        ('SEG', 'Segunda-feira'), ('TER', 'Terça-feira'), ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'), ('SEX', 'Sexta-feira'), ('SAB', 'Sábado'), ('DOM', 'Domingo')
    ]
    titulo = models.CharField(max_length=200)
    dia_semana = models.CharField(max_length=3, choices=DIAS_DA_SEMANA)
    horario = models.TimeField()
    imagem_guerra = models.ImageField(upload_to='guerras_fotos/', blank=True, null=True)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.get_dia_semana_display()}"
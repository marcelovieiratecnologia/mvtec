from django.db import models

# Create your models here.

class Contact(models.Model):
    STATUS = (
        ('Lido', 'Lido'),
        ('Não Lido', 'Não Lido'),
    )

    nome = models.CharField(verbose_name='Nome', max_length=70, blank=False)
    email = models.EmailField(verbose_name='Email', max_length=90, blank=False)
    assunto = models.CharField(verbose_name='Assunto', max_length=120)
    mensagem = models.TextField(verbose_name='Mensagem', blank=False)
    status = models.CharField(choices=STATUS, max_length=14, default="Não Lido")

    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_mvt_contact'  # definindo o nome da tabela, no caso não utilizei deixei o django fazer por mim
        verbose_name = 'Contato'  # 'Entrada/Saída'
        verbose_name_plural = 'Contatos'

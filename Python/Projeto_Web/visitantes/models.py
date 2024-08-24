from django.db import models

class Visitante(models.Model):
    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=255,
    )
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11, 
        unique=True
    )
    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        auto_now=False,
        auto_now_add=False,
    )
    numero_casa = models.CharField(
        verbose_name="Número da Casa Visitada",
        max_length=255,
        blank=True,
    )
    placa_veiculo = models.CharField(
        verbose_name="Placa do Veículo",
        max_length=7, 
        blank=True, 
        null=True,
    )
    hora_chegada = models.DateTimeField(
        verbose_name="Hora de Chegada",
        blank=True, 
        null=True,
        auto_now_add=True,
        )
    hora_saida = models.DateTimeField(
        verbose_name="Hora de Saída",
        blank=True, 
        null=True,
        auto_now=False,
        )
    hora_autorizacao = models.DateTimeField(
        verbose_name="Hora de Autorização",
        blank=True, 
        null=True,
        auto_now=False,
    )
    nome_morador = models.CharField(
        verbose_name="Nome do Morador que autorizou a entrada",
        max_length=255,
        blank=True,
    )
    porteiro_autorizador = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro que Autorizou a Entrada",
        on_delete=models.PROTECT,
      
    )

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"
    
    def __str__(self):
        return self.nome_completo

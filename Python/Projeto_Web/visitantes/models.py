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
    STATUS_VISITANTE = [
        ("AGUARDANDO", "Aguardando autorização"),
        ("EM_VISITA", "Em visita"),
        ("FINALIZADO", "Visita finalizada"),
    ]
    status = models.CharField(
        verbose_name = "Status",
        max_length = 10,
        choices = STATUS_VISITANTE,
        default="AGUARDANDO"
    )
    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"
    
    def __str__(self):
        return self.nome_completo
    
    def get_hora_saida(self):
        if self.hora_saida:
            return self.hora_saida
        return "Horário de saída não registrado"
    
    def get_hora_autorizacao(self):
        if self.hora_autorizacao:
            return self.hora_autorizacao
        return "Horário de Autorização não registrado"
    
    def get_nome_morador(self):
        if self.nome_morador:
            return self.nome_morador
        return "Morador responsável pela autorização não registrado"
    
    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        return "Horário de saída não registrado"

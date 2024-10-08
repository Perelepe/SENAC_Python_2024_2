# Generated by Django 3.0 on 2024-09-04 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_auto_20240814_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitante',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando autorização'), ('EM_VISITA', 'Em visita'), ('FINALIZADO', 'Visita finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='numero_casa',
            field=models.CharField(max_length=255, verbose_name='Número da Casa Visitada'),
        ),
    ]

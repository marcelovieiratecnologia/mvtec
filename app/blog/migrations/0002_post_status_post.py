# Generated by Django 3.1.3 on 2021-04-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status_post',
            field=models.CharField(choices=[('Publicado', 'Publicado'), ('Não Publicado', 'Não Publicado'), ('Arquivado', 'Arquivado')], default='Não Publicado', max_length=14),
        ),
    ]

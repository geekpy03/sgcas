# Generated by Django 3.0.7 on 2020-08-21 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateField(default=datetime.date.today)),
                ('ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Iniciado', 'Iniciado'), ('Cancelado', 'Cancelado'), ('Finalizado', 'Finalizado')], default='Pendiente', max_length=30)),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'permissions': [('crear_proyecto', 'crear_proyecto'), ('iniciar_proyecto', 'iniciar_proyecto'), ('finalizar_proyecto', 'finalizar_proyecto'), ('cancelar_proyecto', 'cancelar_proyecto'), ('ver_proyecto', 'ver_proyecto'), ('eliminar_proyecto', 'eliminar_proyecto'), ('editar_proyecto', 'editar_proyecto'), ('detalles_proyecto', 'detalles_proyecto')],
                'default_permissions': (),
            },
        ),
    ]
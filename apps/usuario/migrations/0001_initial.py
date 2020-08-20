# Generated by Django 3.0.7 on 2020-08-20 01:02

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=False, help_text='Marcar/desmarcar para activar/inactivar cuenta de usuario.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': [('crear_usuario', 'crear_usuario'), ('editar_usuario', 'editar_usuario'), ('agregrar_usuario_proyecto', 'agregrar_usuario_proyecto'), ('eliminar_usuario', 'eliminar_usuario'), ('crear_rol', 'crear_rol'), ('eliminar_rol', 'eliminar_rol'), ('asignar_rol', 'asignar_rol'), ('ver_rol', 'ver_rol'), ('ver_usuarios', 'ver_usuarios'), ('listar_rol', 'listar_rol'), ('editar_rol', 'editar_rol'), ('agregar_usuario_fase', 'agregar_usuario_fase'), ('quitar_usuario_proyecto', 'quitar_usuario_proyecto'), ('quitar_usuario_fase', 'quitar_usuario_fase'), ('mensaje_eliminar', 'mensaje_eliminar'), ('mensaje_editar', 'mensaje_editar'), ('ver_mensaje', 'ver_mensaje')],
                'default_permissions': (),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

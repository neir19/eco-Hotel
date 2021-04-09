# Generated by Django 3.1.7 on 2021-04-04 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Registrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('documento', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('estado', models.CharField(max_length=60)),
                ('observacion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHoraEntrada', models.DateField()),
                ('fechaHoraSalida', models.DateField()),
                ('costoTotal', models.IntegerField()),
                ('observacion', models.CharField(max_length=60)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAl.estado')),
                ('registrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAl.registrador')),
            ],
        ),
    ]

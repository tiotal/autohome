# Generated by Django 2.0.7 on 2018-07-25 02:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.DecimalField(decimal_places=5, max_digits=8)),
                ('umidade', models.DecimalField(decimal_places=5, max_digits=8)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(blank=True, default='OK', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ambiente',
            name='local',
            field=models.ForeignKey(default=1, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='controleambiente.Local'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('camada', models.IntegerField()),
                ('curso', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2022-01-14 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20220114_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
    ]

# Generated by Django 3.2.18 on 2023-03-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_class_sem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_n',
            field=models.CharField(max_length=200),
        ),
    ]

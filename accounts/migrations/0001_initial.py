# Generated by Django 3.2.18 on 2023-03-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Subject', models.CharField(blank=True, max_length=200, null=True)),
                ('Message', models.TextField(blank=True, max_length=400, null=True)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
    ]

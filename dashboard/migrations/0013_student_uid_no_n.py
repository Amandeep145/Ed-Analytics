# Generated by Django 3.2.18 on 2023-03-03 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20230303_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='uid_no_n',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.uid'),
        ),
    ]

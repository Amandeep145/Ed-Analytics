# Generated by Django 3.2.18 on 2023-03-03 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_test_standard_t'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['student_name'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['teacher_name'],
            },
        ),
        migrations.CreateModel(
            name='UID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid_no', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['uid_no'],
            },
        ),
        migrations.RemoveField(
            model_name='marks_data',
            name='No',
        ),
        migrations.AddField(
            model_name='marks_data',
            name='unique_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.uid'),
        ),
        migrations.AlterField(
            model_name='marks_data',
            name='Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.student'),
        ),
    ]
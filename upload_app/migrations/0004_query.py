# Generated by Django 4.2.11 on 2024-03-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=250)),
                ('industry', models.CharField(max_length=250)),
                ('year_founded', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('total_emp', models.CharField(max_length=250)),
                ('current_emp', models.CharField(max_length=250)),
            ],
        ),
    ]
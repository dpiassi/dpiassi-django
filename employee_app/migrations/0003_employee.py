# Generated by Django 4.0.5 on 2022-06-26 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_alter_logmessage_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(verbose_name='created date')),
                ('department', models.CharField(choices=[('UND', 'Undefined'), ('TES', 'Tester'), ('DEV', 'Developer'), ('HR', 'Human Resources')], max_length=3)),
            ],
        ),
    ]

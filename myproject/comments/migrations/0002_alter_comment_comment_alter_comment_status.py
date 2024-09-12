# Generated by Django 5.1.1 on 2024-09-11 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('saved', 'Saved')], default='pending', max_length=250),
        ),
    ]

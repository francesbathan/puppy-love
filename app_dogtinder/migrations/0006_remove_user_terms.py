# Generated by Django 2.2 on 2020-02-27 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_dogtinder', '0005_user_terms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='terms',
        ),
    ]
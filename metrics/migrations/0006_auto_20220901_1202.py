# Generated by Django 2.2.3 on 2022-09-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0005_auto_20200808_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholardata',
            name='ARIndex',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scholardata',
            name='lIndex',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
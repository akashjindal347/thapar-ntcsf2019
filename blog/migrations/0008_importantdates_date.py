# Generated by Django 2.2.2 on 2019-09-03 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190903_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='importantdates',
            name='date',
            field=models.TextField(default=''),
        ),
    ]

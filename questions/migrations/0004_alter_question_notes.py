# Generated by Django 3.2.15 on 2022-10-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20221022_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]

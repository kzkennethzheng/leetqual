# Generated by Django 3.2.15 on 2022-10-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_alter_question_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]

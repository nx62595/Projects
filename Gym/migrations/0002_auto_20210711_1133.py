# Generated by Django 3.2.5 on 2021-07-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gym', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]
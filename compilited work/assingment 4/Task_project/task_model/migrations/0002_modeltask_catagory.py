# Generated by Django 4.2.6 on 2023-12-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_catagory', '0004_remove_catagorymadel_alltitle'),
        ('task_model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltask',
            name='Catagory',
            field=models.ManyToManyField(to='task_catagory.catagorymadel'),
        ),
    ]

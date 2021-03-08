# Generated by Django 2.2.1 on 2020-11-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotationweb', '0004_imageannotation_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='post_processing_method',
            field=models.CharField(blank=True, default='', help_text='Name of post processing method to use', max_length=255),
        ),
    ]

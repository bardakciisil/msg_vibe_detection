# Generated by Django 5.1 on 2024-08-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_message_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='color',
            field=models.CharField(default='#D3D3D3', max_length=7),
        ),
    ]

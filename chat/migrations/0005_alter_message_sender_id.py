# Generated by Django 5.1 on 2024-08-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_message_sender_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender_id',
            field=models.CharField(default='unknown', max_length=255),
        ),
    ]

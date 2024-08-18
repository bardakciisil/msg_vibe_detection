# Generated by Django 5.1 on 2024-08-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_message_sender_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_id',
            field=models.CharField(max_length=255),
        ),
    ]

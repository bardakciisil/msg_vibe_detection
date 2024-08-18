import uuid
import random
from django.core.management.base import BaseCommand
from chat.models import Message

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

class Command(BaseCommand):
    help = 'Create test data for the chat application'

    def handle(self, *args, **kwargs):
        test_messages = [
            ("It's a wonderful day!", uuid.UUID('11111111-1111-1111-1111-111111111111')),
            ("I'm not feeling well today.", uuid.UUID('22222222-2222-2222-2222-222222222222')),
            ("I love this chat app!", uuid.UUID('11111111-1111-1111-1111-111111111111')),
            ("I think I have a problem.", uuid.UUID('33333333-3333-3333-3333-333333333333')),
            ("The weather is gloomy.", uuid.UUID('22222222-2222-2222-2222-222222222222')),
        ]

        for content, sender_id in test_messages:
            color = random_color()
            Message.objects.create(content=content, sender_id=str(sender_id), color=color)

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))

from django.core.management.base import BaseCommand
from chat.models import Message

class Command(BaseCommand):
    help = 'Create test data for the chat application'

    def handle(self, *args, **kwargs):
        # Test messages
        test_messages = [
            ("It's a wonderful day!", '11111111-1111-1111-1111-111111111111'),
            ("I'm not feeling well today.", '22222222-2222-2222-2222-222222222222'),
            ("I love this chat app!", '11111111-1111-1111-1111-111111111111'),
            ("I think I have a problem.", '33333333-3333-3333-3333-333333333333'),
            ("The weather is gloomy.", '22222222-2222-2222-2222-222222222222'),
        ]

        for content, sender_id in test_messages:
            Message.objects.create(content=content, sender_id=sender_id)

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))

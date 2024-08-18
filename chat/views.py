import uuid
from django.shortcuts import render
from .models import Message
from textblob import TextBlob
import random

# Define a dictionary to store session colors
SESSION_COLORS = {}

def analyse_vibe(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def get_color_for_session(session_id):
    if session_id not in SESSION_COLORS:
        SESSION_COLORS[session_id] = random_color()
    return SESSION_COLORS[session_id]

def random_color():
    hex_color = f"#{random.randint(0, 0xFFFFFF):06X}"  
    return hex_color[:7]


def chat(request):
    if 'session_id' not in request.session:
        request.session['session_id'] = str(uuid.uuid4())
    sender_id = request.session['session_id']
    last_message_content = request.session.get('last_message_content')     

    if request.method == 'POST':
        content = request.POST.get('message')
        if content and last_message_content != content:
            color = get_color_for_session(sender_id)
            Message.objects.create(content=content, sender_id=sender_id, color=color)
            request.session['last_message_content'] = content

    messages = Message.objects.all().order_by('timestamp')
    vibes = [analyse_vibe(msg.content) for msg in messages]
    message_vibes = zip(messages, vibes)
    
    return render(request, 'chat/chat.html', {
        'message_vibes': message_vibes,
    })

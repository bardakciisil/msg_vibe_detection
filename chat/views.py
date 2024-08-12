import uuid
from django.shortcuts import render
from .models import Message
from textblob import TextBlob

def analyse_vibe(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # the val returns [-1,1] - :( +:)

def chat(request):
    if 'session_id' not in request.session:
        request.session['session_id'] = str(uuid.uuid4())  
    sender_id = request.session['session_id']
    last_message_content = request.session.get('last_message_content')       

    if request.method == 'POST':
        content = request.POST.get('message')
        if content and last_message_content != content:
            Message.objects.create(content=content, sender_id=sender_id)
            request.session['last_message_content'] = content
    if last_message_content in request.session:
        del request.session['last_message_content']
        request.session['last_message_content'] = 0

    messages = Message.objects.all().order_by('timestamp')

    # NLP analysis
    vibes = [analyse_vibe(msg.content) for msg in messages]
    #merge messages and vibe lists
    message_vibes = zip(messages, vibes)

    return render(request, 'chat/chat.html', {
        'message_vibes': message_vibes,
    })

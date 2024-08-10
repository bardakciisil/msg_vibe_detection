import uuid
from django.shortcuts import render
from .models import Message

def chat(request):
    if 'session_id' not in request.session:
        request.session['session_id'] = str(uuid.uuid4())  

    if request.method == 'POST':
        content = request.POST.get('message')
        if content:
            sender_id = request.session['session_id']
            last_message_content = request.session.get('last_message_content')
            if last_message_content != content:
                Message.objects.create(content=content, sender_id=sender_id)
                request.session['last_message_content'] = content
    if last_message_content in request.session and sender_id == request.session['session_id']:
        del request.session['last_message_content']

    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'chat/chat.html', {'messages': messages})

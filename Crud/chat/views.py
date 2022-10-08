from django.shortcuts import render, redirect
from .models import Profile, Friend,ChatMessage
from .forms import ChatMessageForm
# Create your views here.


def lobby(request):
    return render(request, 'chat/lobby.html')


def client(request):
    user = request.user.profile
    friends = user.friends.all()
    context = {'user': user, 'friends': friends}
    return render(request, 'chat/client.html', context)


def detail(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id=friend.profile.id)
    chats= ChatMessage.objects.all()
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect("friend", pk=friend.profile.id)
    context = {"friend": friend, "form": form,
               "user": user, "profile": profile, "chats":chats}
    return render(request, 'chat/friend.html', context)

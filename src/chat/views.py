from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import JsonResponse
import random
import time
import json

from . models import RoomMember

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    # member, created = RoomMember.objects.get_or_create(
    #     user=request.user,
    #     room_name = room_name
    # )
    room_users = RoomMember.objects.filter(room_name = room_name)
    return render(request, "chat/room.html", {"room_name": room_name, 'room_users':room_users})




def deleteMember(request):
    print("delet memeber")
    room_name =  request.GET.get('room_name')
    member = RoomMember.objects.get(
        user = request.user,
        room_name = room_name
    )
    member.delete()
    return redirect('index')


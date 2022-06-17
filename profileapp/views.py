from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from . serializers import ProfileSerializer,EducationSerializer
from .models import Profile , Education
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import CreateUserForm, ProfileForm
from rest_framework import viewsets
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return render(request, 'home.html')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form':form}
    return render(request, 'profile.html', context)

@unauthenticated_user
def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect('home')
        else:
            messages.info(request, 'Wrong passwrod or username')
            return redirect('login')
    return render(request, 'login_page.html')

@unauthenticated_user
def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('login')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'register_page.html', context)

    context = {'form': form}
    return render(request, 'register_page.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('login')

class profilelist(viewsets.ViewSet):
    def list(self,request):
        p=Profile.objects.all()
        ser=ProfileSerializer(p,many=True)
        return Response(ser.data)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            p=Profile.objects.get(id=id)
            serial=ProfileSerializer(p)
            return Response(serial.data)

class ProfileView(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class =EducationSerializer

class Vi(APIView):
    queryset=Profile.objects.all()
    serializer=ProfileSerializer
@api_view(['GET'])
def list(request):
    a1 = Profile.objects.all()
    serial=ProfileSerializer(a1,many=True)
    return Response(serial.data)
@api_view(['POST'])
def createlist(request):
    serial=ProfileSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)
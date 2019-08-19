from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .oauth import get_discord_name, get_faceit_name

@login_required
def account(request):
    return render(request, 'settings/account.html')

@login_required
def faceit(request):
    faceit_code = request.GET.get('code')

    if (faceit_code == None):
        return redirect('account')

    faceit_username = get_faceit_name(faceit_code)

    # Enter faceit name into user profile
    user = User.objects.get(username=request.user.username)
    user.profile.faceit = faceit_username
    user.save()

    return redirect('account')
    
@login_required
def discord(request):
    discord_code = request.GET.get('code')

    if (discord_code == None):
        return redirect('account')

    discord_name = get_discord_name(discord_code)

    # Enter discord name into user profile
    user = User.objects.get(username=request.user.username)
    user.profile.discord = discord_name
    user.save()
    return redirect('account')
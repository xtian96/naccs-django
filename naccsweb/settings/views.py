from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .oauth import get_discord_name, get_faceit_name
from .schools import get_schools
from .forms import CollegeForm

@login_required
def account(request):
    schools = get_schools()

    if request.method == 'POST':
        form = CollegeForm(request.POST, schools=schools)
        
        if form.is_valid():
            print("Is valid!")
            print(form.cleaned_data['college'])
            print(form.cleaned_data['email'])
    else:
        form = CollegeForm(schools=schools)
    

    return render(request, 'settings/account.html', {'form': form})

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
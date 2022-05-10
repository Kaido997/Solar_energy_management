from time import sleep
from django.shortcuts import render, redirect
from energy.models import Solar_energy
from django.contrib.auth import authenticate, login, logout
from energy.view_utils import get_total, check_admin_ip, get_admin_ip_from, set_new_admin_ip
from datetime import timedelta
from django.utils.timezone import now

def homepage(request):
    '''Homepage security and login logic'''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            ip = get_admin_ip_from(request)
            if ip:
                if check_admin_ip(ip):
                    try:
                        data = Solar_energy.objects.order_by('-time')
                        latest = Solar_energy.objects.latest('time')
                        return render(request, 'energy/data.html', 
                        {'data': data, 'last_transaction': latest, 'total_produced': get_total('produced'), 'total_consumed': get_total('consumed')})
                    except:
                        return render(request, 'energy/data.html')
                else:
                    return redirect('secure')
            else:
                return render(request, 'energy/data.html')
        else:
            return redirect('homepage')
    else:
        if request.user.is_authenticated:
            try:
                data = Solar_energy.objects.order_by('-time')
                latest = Solar_energy.objects.latest('time')
                return render(request, 'energy/data.html', 
                {'data': data, 'last_transaction': latest, 'total_produced': get_total('produced'), 'total_consumed': get_total('consumed')})
            except:
                return render(request, 'energy/data.html')
        else:
            return render(request, 'energy/login.html')


def log_out(request):
    logout(request)
    return redirect('homepage')


def getNewData(request):
    if request.user.is_authenticated:
        try:
            latest = Solar_energy.objects.latest('time')
            sleep(5)
            if int((latest.time+timedelta(days=1)).strftime('%d')) -  int(now().strftime('%d')) < 0:
                newObj = Solar_energy()
                newObj.newData()
                return redirect('homepage')
            else:
                return redirect('homepage')
        except Solar_energy.DoesNotExist:
            new = Solar_energy()
            new.newData()
            return redirect('homepage')


def secure(request):
    if request.method == 'POST':
        ip = request.META['REMOTE_ADDR']
        set_new_admin_ip(ip)
    return redirect('homepage')
        


# Create your views here.

from django.shortcuts import render, redirect
from energy.models import Solar_energy
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from energy.view_utils import get_total, check_admin_ip, get_admin_ip_from, set_new_admin_ip


def homepage(request):

    if request.user.is_authenticated:
        try:
            data = Solar_energy.objects.order_by('-time')
            latest = Solar_energy.objects.latest('time')
            paginator = Paginator(data, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'energy/data.html', 
            {'data': data, 'last_transaction': latest, 'total_produced': get_total('produced'), 'total_consumed': get_total('consumed'), 'page_obj': page_obj})
        except:
            return render(request, 'energy/data.html')
    else:
        return redirect("log_in")

def log_out(request):
    logout(request)
    return redirect('log_in')

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff:
                ip = get_admin_ip_from(request)
                if ip:
                    if check_admin_ip(ip):
                        return redirect('homepage')
                else:
                    logout(request)
                return redirect('secure')
            else:
                return redirect('homepage')
        else:
            return redirect('log_in')
    else:
        return render(request, 'energy/login.html')

def secure(request):
    if request.method == 'POST':
        ip = request.META['REMOTE_ADDR']
        set_new_admin_ip()
        return redirect('homepage')
    else:
        ip = request.META['REMOTE_ADDR']
        if request.user.is_authenticated and check_admin_ip(ip):
            return redirect('homepage')
        else:
            return render(request, 'energy/security.html')
        

# Create your views here.

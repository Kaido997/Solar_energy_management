from energy.models import Solar_energy
import redis
from datetime import timedelta
from django.utils.timezone import now


def get_total(type):
    '''Simple function to get the totals amoutns of energy'''
    if type == "consumed":
        total_C = 0
        data =  Solar_energy.objects.order_by('time')
        for i in data:
            total_C += i.consumed
        return total_C
    elif type == "produced":
        total_P = 0
        data =  Solar_energy.objects.order_by('time')
        for i in data:
            total_P += i.produced
        return total_P


def check_admin_ip(ip):
    redisS = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8",decode_responses=True)
    check_ip = redisS.get('admin_ip')
    if check_ip is not None:
        if check_ip == ip:
            return True
        else:
            return False
    else:        
        redisS.set('admin_ip', ip)
        return True

def get_admin_ip_from(request):
    redisS = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8",decode_responses=True)
    if request.user.is_staff:
        admin_ip = request.META['REMOTE_ADDR']
        redisS.set('temp_ip', admin_ip)
        return admin_ip
    else:
        pass

def set_new_admin_ip():
    redisS = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8",decode_responses=True)
    new_ip = redisS.get('temp_ip')
    redisS.set('admin_ip', new_ip)


def get_delay_time(tempo):
    try:
        latest = Solar_energy.objects.latest('time')
    except Solar_energy.DoesNotExist:
        return 0
    arrival = latest.time + timedelta(seconds=tempo)
    delay = arrival - latest.time
    if arrival < now():
        return 0
    elif delay.total_seconds() > 0:
        return  int(delay.total_seconds())
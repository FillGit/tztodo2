import binascii
import string
import random
import datetime
from todo.models import Desks, CompanyName, Profile
from django.contrib.auth.models import User
from datetime import datetime

def idsession_generator(size=8, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

def check_auth(key_idsession_f, companyname):
        
        
        if Profile.objects.filter(idsession=key_idsession_f, active_company=companyname).count()==1:
                modProfile=Profile.objects.get(idsession=key_idsession_f)

                now = datetime.now()
                check_date_idsession=(now.strftime("%Y-%m-%d")==str(modProfile.date_idsession))

                if check_date_idsession:
                        return True
                else:
                        return False


def check_auth_user_params(pk, key_auth_user_f):
        str_decode = query_de(key_auth_user_f).split('/')

        username=str_decode[0]
        password=str_decode[1]
        date_password=str_decode[2]

        user_obj=User.objects.get(username=username)
        modProfile=Profile.objects.get(user=user_obj)

        if (check_password(password, user_obj.password)):
                modProfile.time_password=time_password_generator()
                modProfile.date_password=now.strftime("%d-%m-%Y")
                modProfile.active_company=pk
                return True
        else:
                return False

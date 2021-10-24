from . models import *
from . views import *
def count(request):
    item_count=0
    if 'admin 'in request.path:
        return {}
    else:
        try:
            ct=cart.objects.filter(cart_id=c_id(request))
            cti=cartitem.objects.all().filter(cart=ct[:1])
            for i in cti:
                item_count +=i.qty
        except cart.DoesNotExist:
            item_count=0
        return dict(itc=item_count)
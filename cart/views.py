from django.shortcuts import render,redirect,get_object_or_404
from home.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist
def cartdet(request,tot=0,count=0,ct_items=None):
    try:
        ct=cart.objects.get(cart_id=c_id(request))
        ct_items=cartitem.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot += (i.prod_seltd.price*i.qty)
    except ObjectDoesNotExist:
        pass

    return render(request,'index c.html',{'ci':ct_items,'t':tot,'cn':count})

def c_id(request):
    crt_id=request.session.session_key
    if not crt_id:
        crt_id=request.session.create()
    return crt_id

def cart_add(request,prdct_id):
    pro=prdct.objects.get(id=prdct_id)
    try:
        id=cart.objects.get(cart_id=c_id(request))
    except cart.DoesNotExist:
        id=cart.objects.create(cart_id=c_id(request))
        id.save()
    try:
        c_items=cartitem.objects.get(prod_seltd=pro,cart=id)
        if c_items.qty <  c_items.prod_seltd.stock:
            c_items.qty+=1
        c_items.save()
    except cartitem.DoesNotExist:
        c_items = cartitem.objects.create(prod_seltd=pro, qty=1, cart=id)
        c_items.save()
    return redirect('cartdet')

def cart_min(request,prdct_id):
    crt=cart.objects.get(cart_id=c_id(request))
    pro=get_object_or_404(prdct,id=prdct_id)
    c_item=cartitem.objects.get(prod_seltd=pro,cart=crt)
    if c_item.qty >1 :
        c_item.qty-=1
        c_item.save()
    else:
        c_item.delete()
    return redirect('cartdet')

def cart_remove(request,prdct_id):
    crt=cart.objects.get(cart_id=c_id(request))
    pro=get_object_or_404(prdct,id=prdct_id)
    c_item=cartitem.objects.get(prod_seltd=pro,cart=crt)
    c_item.delete()
    return redirect('cartdet')
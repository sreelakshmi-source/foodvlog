from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request,c_slug=None):
    c_page = None
    pro = None
    if c_slug!= None:
        c_page=get_object_or_404(categ,slug=c_slug)
        pro=prdct.objects.filter(category=c_page,avialable=True)
    else:
        pro=prdct.objects.all().filter(avialable=True)

    categs = categ.objects.all()

    paginator=Paginator(pro,3) # dividing objects in var pro to division of '3'
    try:
        page=int(request.GET.get('page','1')) # getting page requested in var page or page 1 default and convert to int
    except:
        page=1
    try:
        prog=paginator.page(page) # from var paginator (containing pages 1,2,3,...) getting specific page in var 'page'
    except(EmptyPage,InvalidPage): # if entered any irrelevant page
        prog=paginator.page(paginator.num_pages)# query to show or get all page numbers

    return render(request, "index h.html", {'categs': categs, 'pros': pro,'pg':prog })


def details(request,c_slug,pro_slug):
    try:
        pro=prdct.objects.get(category__slug=c_slug,slug=pro_slug )
    except Exception as e:
        raise e
    return render(request,"index p.html",{'pro':pro})

def search(request):
    pro=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')  # gets q in request to query
        pro=prdct.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query)) # filters objects of prdct model if its "name or desc field" contains  letters inquery

    return render (request,'search.html',{'que':query,'pro':pro})

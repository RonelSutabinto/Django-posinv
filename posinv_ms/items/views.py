import math, datetime, time, json, json as json_util
from django.db import connection
from django.db.models.expressions import Window
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from .models import items, itemserials, itemserials_details, category
from django.db.models.query_utils import Q
from .forms import categoryForm, itemForm #, itemserialsForm, serialsdetailsForm

from django.views.generic import CreateView, FormView, RedirectView, ListView
from django.utils.dateparse import parse_datetime

# Create your views here.

datetoday = datetime.date.today()

header = 'Dashboard'

# Create your views here.
class IIIViews(ListView):
    model = items
    html = 'items/item_list.html'
    success_url = '/'
        
    #def get_queryset(self):        
    #    return self.model.objects.filter(
           # itemcode__icontains=self.request.GET.get('filter') ,              
    #        name__icontains=self.request.GET.get('filter'),).values('id','itemcode','name','description','brand','category','unit','qty','price','saleprice','pricingdate').order_by( self.request.GET.get('order_by') )

    
    def get_queryset(self):        
        query = self.request.GET.get('filter')
        return self.model.objects.filter((Q(name__icontains=query) | Q(itemcode__icontains=query) | Q(category__icontains=query) | Q(brand__icontains=query) ) & Q(active__icontains=1)).values('id','itemcode','name','description','brand','category','unit','qty','price','saleprice','pricingdate').order_by( self.request.GET.get('order_by') )
            
         
    ''' source of class statement==============
    class SearchedPostListView(ListView):
        model = Post
        template_name = 'blog/search.html'  # /_.html
        paginate_by = 2
        context_object_name = 'posts'   
    
        def get_context_data(self, *args, **kwargs):
            context = super(SearchedPostListView, self).get_context_data(*args, **kwargs)
            query = self.request.GET.get('q')
            context['posts'] = Post.objects.filter(Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query))
            context['categories'] = Categories.objects.all
            return context'''

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            start = int(request.GET.get('start'))
            limit = int(request.GET.get('limit'))
            filter = request.GET.get('filter')
            
            list_data = []
            for index, _item in enumerate(self.get_queryset()[start:start+limit], start):                
                list_data.append(_item)
                                    
           
            data = {
                'length': self.get_queryset().count(),
                'objects': list_data,
            }
            return HttpResponse(json.dumps(data, default=default), 'application/json')
        else:
            return render(request, self.html, {'header': 'Item Index'})
    
def delete_items(request, id):
    if request.is_ajax():
        id = request.GET.get('id')
        iteminfo = items.objects.get(pk=id)
        iteminfo.delete()
        json_response = {json.dumps('deleted')}
    return HttpResponse(json_response, content_type='application/json')


# class MeterList(CreateView):
def add_item(request):
    category_set = category.objects.all()    
    #form =categoryForm()
    # serials = meterserials.objects.filter(idmeters=id).filter(wms_status__exact=0)
    context = {#'form': form, 
                'category': category_set,
                'header':'Item Index / Add Item'}    
    
    return render(request, 'items/add_item.html',context)

def save_item(request):
    category_set = category.objects.all()   
    context = {'category': category_set,
                'header':'Item Index / Add Item'}  

    if request.method == "POST":
        form = itemForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()                
                return render(request,'items/add_item.html',context)
            except:
                pass
    else:
        form = itemForm()
    return render(request,'items/add_item.html',context)
    
    #return render(request, 'items/add_item.html',context)
'''def additem(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                items = Item.objects.all()     
                return render(request,'datatables/itemlist_dt.html',{'items': items,
                                                                     'msgEvent': "success add",
                                                                     'msg_record': "Item record successfully added."
                })          
                
            except:
                pass
    else:
        form = ItemForm()
    return render(request,'additemindex.html',{'form':form})
def save_item(request):
    if request.is_ajax():
        itemcode = request.GET.get('itemcode_tf')
        name = request.GET.get('name_tf')
        description = request.GET.get('description_tf')
        brand = request.GET.get('brand_tf')
        category = request.GET.get('category_tf')

        cursor = connection.cursor()        
        cursor.execute('insert into invpos_ms.items(itemcode,name,description,brand,category,unit) values("'+itemcode+'","'+name+'","'+description+'","'+brand+'","'+category+'","pcs") ')
        cursor.fetchall()

        category_set = category.objects.all()   
        context = {'category': category_set,
                   'header':'Item Index / Add Item'}    
    
    return render(request, 'items/add_item.html',context)'''

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


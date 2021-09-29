import math, datetime, time, json, json as json_util
from django.db import connection
from django.db.models.expressions import Window
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from .models import items, itemserials, itemserials_details
from django.db.models.query_utils import Q
from .forms import itemForm #, itemserialsForm, serialsdetailsForm

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
    '''
    def get(self):
        if request.is_ajax():
            start = int(request.GET.get('start'))
            limit = int(request.GET.get('limit'))
            filter = request.GET.get('filter')
            order_by = request.GET.get('order_by')
            query = self.model.objects.filter( Q(itemcode__icontains=self.request.GET.get('filter')) |
            Q(name__icontains=self.request.GET.get('filter')),
            ).values('id','itemcode','name','description','brand','category',
            'unit','qty','price','saleprice','pricingdate').order_by( self.request.GET.get('order_by') )

            list_data = []
            for index, _item in enumerate(query[start:start+limit], start):
                list_data.append(_item)
            data = {
                'length': query.count(),
                'objects': list_data,
            }
            return HttpResponse(json.dumps(data, default=default), 'application/json')
        else:
            return render(request, self.html, {'header': 'Stock List'})'''

def delete_items(request, id):
    if request.is_ajax():
        id = request.GET.get('id')
        iteminfo = items.objects.get(pk=id)
        iteminfo.delete()
        json_response = {json.dumps('deleted')}
    return HttpResponse(json_response, content_type='application/json')


# class MeterList(CreateView):
def add_item(request):
    return render(request, 'items/add_item.html', {'id': id, 'header':'Item Index / Add Item'})

def seriallist_data(request, id):
    if request.is_ajax():
        '''start = int(request.GET.get('start'))
        limit = int(request.GET.get('limit'))
        filter = request.GET.get('filter')
        order_by = request.GET.get('order_by')
        query = itemserials.objects.select_related('items').filter(id=id,
            serialno__icontains=filter,).values('id', 'itemcode', 'name', 'description',
                                            'brand', 'category', 'unit', 'qty', 'price','saleprice').order_by(order_by)
        
        list_data = []
        for index, item in enumerate(query[start:start+limit], start):
            list_data.append(item)'''
        data = {
            'length': 2,#query.count(),
            'objects': [{'id' : '1', 'dateforwarded' : '2021-10-21', 'rrnumber' : '1001','brand' : 'brand'}],#list_data,
        }
        return HttpResponse(json.dumps(data, default=default), 'application/json')


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

'''
def selected_serial(request):
    if request.is_ajax():
        id = request.GET.get('iditems')
        idmeters = request.GET.get('itemcode')
        queryset = itemserials_details.objects.filter(idmeterserials=id).order_by('iditemsserials')
        html = 'items/list_serials_ext.html'
        context = {'trans': queryset, 'iditems': id, 'itemcode': idmeters}
        return render(request, html, context)


def edit_items(request, id, idmeters):
    if request.method == "POST":
        queryset = meterserials_details(pk=id)
        form = serialsdetailsForm(request.POST, instance=queryset)
        if form.is_valid():
            created = request.POST.get('created_at')
            print(parse_datetime(created))
            rec = form.save(commit=False)
            rec.created_at = datetoday
            rec.save()

            cursor = connection.cursor()
            idmeterserials = request.POST['idmeterserials']
            average = request.POST['gen_average']
            cursor.execute(
                'update zanecometerpy.meter_serials set wms_status=1, status = if("' + str(average) + '" >= 98,1,2), accuracy="' + str(average) + '" where id = "' + str(idmeterserials) + '"')
            cursor.fetchall()
        return redirect("../../")
    else:
        queryset = meterserials_details.objects.get(pk=id)
        serials = meterserials.objects.get(id=idmeters)
        # serials = meterserials.objects.select_related(
        #     "meter_serials").filter(id=idmeters)
        context = {'form': queryset, 'datetoday': datetoday, 'serials': serials}
        return render(request, 'meters/calibration_edit.html', context)'''
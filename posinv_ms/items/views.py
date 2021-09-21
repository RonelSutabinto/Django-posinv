import math, datetime, time, json, json as json_util
from django.db import connection
from django.db.models.expressions import Window
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from .models import items, itemserials, itemserials_details
from .forms import itemForm #, itemserialsForm, serialsdetailsForm

from django.views.generic import CreateView, FormView, RedirectView, ListView
from django.utils.dateparse import parse_datetime

# Create your views here.

datetoday = datetime.date.today()

header = 'Dashboard'

# Create your views here.
class iViews(ListView):
    model = items
    html = 'items/item_list.html'
    success_url = '/'

    def get_queryset(self):
        return self.model.objects.filter(
            serialnos__icontains=self.request.GET.get('filter'),
            rrnumber__icontains=self.request.GET.get('filter'),).values('iditems','itemcode','name','description','brand','category','unit','qty','price','saleprice','pricingbyID','pricingdate').order_by( self.request.GET.get('order_by') )

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            start = int(request.GET.get('start'))
            limit = int(request.GET.get('limit'))
            filter = request.GET.get('filter')
            # order_by = request.GET.get('order_by')
            list_data = []
            for index, item in enumerate(self.get_queryset()[start:start+limit], start):
                list_data.append(item)
            data = {
                'length': self.get_queryset().count(),
                'objects': list_data,
            }
            return HttpResponse(json.dumps(data, default=default), 'application/json')
        else:
            return render(request, self.html, {'header': 'items'})


def delete_items(request, id):
    if request.is_ajax():
        id = request.GET.get('iditem')
        iteminfo = items.objects.get(pk=id)
        iteminfo.delete()
        json_response = {json.dumps('deleted')}
    return HttpResponse(json_response, content_type='application/json')


# class MeterList(CreateView):
def seriallist(request, id):
    return render(request, 'meters/list_serials.html', {'idmeters': id, 'header':'List of Meter Serial'})

def seriallist_data(request, id):
    if request.is_ajax():
        start = int(request.GET.get('start'))
        limit = int(request.GET.get('limit'))
        filter = request.GET.get('filter')
        order_by = request.GET.get('order_by')
        query = itemserials.objects.select_related('items').filter(idmeters=id,
            serialno__icontains=filter,).values('iditems', 'itemcode', 'serialno', 'ampheres',
                                            'accuracy', 'wms_status', 'status', 'active', 'userid').order_by(order_by)
        list_data = []
        for index, item in enumerate(query[start:start+limit], start):
            list_data.append(item)
        data = {
            'length': query.count(),
            'objects': list_data,
        }
        return HttpResponse(json.dumps(data, default=default), 'application/json')


def selected_serial(request):
    if request.is_ajax():
        id = request.GET.get('iditems')
        idmeters = request.GET.get('itemcode')
        queryset = itemserials_details.objects.filter(idmeterserials=id).order_by('iditemsserials')
        html = 'items/list_serials_ext.html'
        context = {'trans': queryset, 'iditems': id, 'itemcode': idmeters}
        return render(request, html, context)

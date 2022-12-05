from django.shortcuts import render
from app.models import Workson
from django.db.models import Count
from django.db.models import Sum
# Create your views here.

    
def report_view(request):
    data = Workson.objects.annotate(duration=Sum('Duration'))
    context= {'data': data,}
    return render (request, 'report.html', context)
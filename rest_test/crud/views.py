from django.shortcuts import render, redirect
from .models import GenListItem
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def crud(request):
    
    if request.method == 'POST':         
        try:
            genitems = GenListItem()
            genitems.items = request.POST['item']
            
            genitems.save()
        except KeyError:
            pass   
        try:
            
            list_id = request.POST.get('listid')
            get_item = GenListItem.objects.get(pk=list_id.split('-')[-1])
            get_item.items = str(request.POST.get('replace'))
            get_item.save()
        except (TypeError,KeyError,AttributeError):
            pass
        
        try:
            
            del_id =  request.POST.get('delid')
            del_item = GenListItem.objects.get(pk=del_id.split('-')[-1])
            del_item.delete()
        except (TypeError,AttributeError):
            pass 
          
    list_entries={}
    for items,id in zip(GenListItem.objects.all(), [itemid.id for itemid in GenListItem.objects.all()]):
            list_entries[id] = items  
      
    list_data = {'data':list_entries }
    return render(request, 'crud/crud.html', list_data)



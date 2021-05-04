from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import assetOwner
#from .resources import AssetResources
from tablib import Dataset

def emp(request):
    form=asset()
    if request.method=="POST":
        form=asset(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('/view')
            return redirect('view1')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'addUser'}}">reload</a>""")
    else:
        form=asset()
        return render(request,'asset.html',{'form':form})

def view(request):
    assets=assetOwner.objects.all()
    return render(request, "view.html" ,{'assets': assets})

def delete(request,asset_id):
    asset_id=int(asset_id)
    try:
        assets=assetOwner.objects.get(id=asset_id)
    except assetOwner.DoesNotExist:
        return redirect('view')
    assets.delete()
    return redirect('view')


def edit(request,asset_id):
    asset_id=int(asset_id)
    try:
        assets = assetOwner.objects.get(id=asset_id)
    except assetOwner.DoesNotExist:
        return redirect('view')
    asset_form=asset(request.POST or None, instance =assets)
    if asset_form.is_valid():
        asset_form.save()
        return redirect('view')
    return render(request, 'asset.html',{'form':asset_form})



def excel_upload(request):
    return render(request, 'excel.html')
#    if request.method=='POST':
#        asset_resource=AssetResources()
#        dataset=Dataset()
#        new_asset=request.FILES['myFile']

        ## file validation
#        if not new_asset.name.endswith('xlsx'):
#            messages.info(request,'wrong format')
#            return render(request,'upload.html')
#        imported_data=dataset.load(new_asset.read(),format='xlsx')
#        for data in imported_data:
#            value=assetOwner(
#                data[0],
#                data[1],
#                data[2],
#                data[3],
#                data[4],
#                data[5],
#                data[6],
#                data[7],
#                data[8]
#            )
#            value.save()

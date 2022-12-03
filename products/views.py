from django.shortcuts import render,redirect,HttpResponse
from .models import Product
from .forms import ProductForm
from registration import views
from registration import urls
from django.contrib.auth.decorators import login_required
# Create your views here.
#product CRUD views
def products_list(request):
    products=Product.objects.all()
    context = {'products':products}
    return render(request,'products/list.html',context)

    
@login_required
def products_detail(request,id):
    product=Product.objects.get(id=id)
    context = {'product':product}
    return render(request,'products/detail.html',context)

@login_required
def products_create(request):
    form=ProductForm()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')
        else:
            print(form.errors)
    context = {'form':form}
    return render(request,'products/create.html',context)

@login_required  
def products_update(request,id):
    product=Product.objects.get(id=id)
    form=ProductForm(instance=product)
    if request.method == 'POST':
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_list')
        else:
            print(form.errors)

    context = {'form':form} 
    return render(request,'products/update.html',context)

def products_delete(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('products_list')
    

    

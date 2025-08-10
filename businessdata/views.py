from django.shortcuts import render, redirect
from .forms import BusinessForm
from .models import Business

def business_list(request):
    businesses = Business.objects.all().order_by('-created_at')
    return render(request, 'business_list.html', {'businesses': businesses})

def add_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business_list')
    else:
        form = BusinessForm()
    return render(request, 'businessdata/add_business.html', {'form': form})

from django.shortcuts import render,redirect,get_object_or_404
from .models import Kategori,Artikel
from .forms import KategoriForm,ArtikelForm

def kategori_list(request):
    kategori = Kategori.objects.all()
    return render(request,'kategori_list.html',{'kategori':kategori})

def kategori_create(request):
    form = KategoriForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('kategori_list')
    return render(request,'kategori_form.html',{'form':form})

def kategori_delete(request,id):
    data = get_object_or_404(Kategori,id=id)
    data.delete()
    return redirect('kategori_list')

def artikel_list(request):
    artikel = Artikel.objects.all()
    return render(request,'artikel_list.html',{'artikel':artikel})

def artikel_create(request):
    form = ArtikelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('artikel_list')
    return render(request,'artikel_form.html',{'form':form})

def artikel_detail(request,id):
    artikel = get_object_or_404(Artikel,id=id)
    return render(request,'artikel_detail.html',{'artikel':artikel})

def artikel_delete(request,id):
    artikel = get_object_or_404(Artikel,id=id)
    artikel.delete()
    return redirect('artikel_list')

from django import forms
from .models import Kategori,Artikel

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama']

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul','isi','kategori']

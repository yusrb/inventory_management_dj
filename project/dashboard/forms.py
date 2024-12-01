from django import forms
from .models import (
  Produk,
  Pemesanan,
)

class ProdukCreationForm(forms.ModelForm):
  class Meta:
    model = Produk
    fields = ['nama', 'kategori', 'kuantitas']

class PemesananCreationForm(forms.ModelForm):
  class Meta:
    model = Pemesanan
    fields = ['produk', 'pemesanan_kuantitas']
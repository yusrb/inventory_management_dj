from django.contrib import admin
from django.contrib.auth.models import Group
from .models import (
  Produk,
  Kategori,
  Pemesanan,
)

admin.site.site_header = "Bvrsk  Inventory Dashboard"

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
  list_display = ('nama', 'kategori', 'kuantitas')
  list_filter = ('kategori',)

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
  pass

@admin.register(Pemesanan)
class PemesananAdmin(admin.ModelAdmin):
  list_display = ('produk', 'pemesanan_kuantitas', 'staff', 'tgl_pemesanan',)
  list_filter = ('staff',)

# admin.site.unregister(Group)
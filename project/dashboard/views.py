from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
  Produk,
  Pemesanan,
)
from user import models as user_models
from .forms import (
  ProdukCreationForm,
  PemesananCreationForm
)
from django.contrib import messages

@login_required
def index(request):
  pesanan = Pemesanan.objects.filter(staff = request.user.pk)
  all_pesanan = Pemesanan.objects.all()
  produk = Produk.objects.all()

  total_staff = user_models.User.objects.all().count()
  total_product = Produk.objects.all().count()
  total_order = Pemesanan.objects.all().count()

  if request.method == "POST":
    pemesanan_form = PemesananCreationForm(request.POST)
    if pemesanan_form.is_valid:
      instance = pemesanan_form.save(commit=False)
      instance.staff = request.user
      instance.save()
      nama_produk = pemesanan_form.cleaned_data.get('produk')
      messages.success(request, f'{nama_produk} Berhasil Ditambah!')
      redirect('dashboard:dashboard_index')
  else:
    pemesanan_form = PemesananCreationForm()

  context = {
    'pesanans': pesanan,
    'all_pesanan': all_pesanan,
    'produks': produk,
    'pemesanan_form': pemesanan_form,
    'total_staff': total_staff,
    'total_product': total_product,
    'total_order': total_order,
  }
  return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
  staff = user_models.User.objects.all()
  total_staff = user_models.User.objects.all().count()
  total_product = Produk.objects.all().count()
  total_order = Pemesanan.objects.all().count()

  context = {
    'staffs':staff,
    'total_staff': total_staff,
    'total_product': total_product,
    'total_order': total_order,
  }
  return render(request, 'dashboard/staff.html',context)

@login_required
def staff_detail(request, pk):
  staff = user_models.User.objects.get(id=pk)

  context = {
    'staff': staff
  }

  return render(request, 'dashboard/staff_detail.html', context)

@login_required
def product(request):
  produks = Produk.objects.all()
  total_staff = user_models.User.objects.all().count()
  total_product = Produk.objects.all().count()
  total_order = Pemesanan.objects.all().count()

  if request.method == 'POST':
    produk_form = ProdukCreationForm(request.POST)
    if produk_form.is_valid():
      produk_form.save()
      nama_produk = produk_form.cleaned_data.get('nama')
      messages.success(request, f'{nama_produk} berhasil ditambahkan!')
      return redirect('dashboard:dashboard_product')
  else:
    produk_form = ProdukCreationForm()
  context = {
    'produks': produks,
    'produk_form': produk_form,
    'total_staff': total_staff,
    'total_product': total_product,
    'total_order': total_order,
  }

  return render(request, 'dashboard/product.html', context)

@login_required
def product_del(request, pk):
  produk = Produk.objects.get(id=pk)
  if request.method == 'POST':
    produk.delete()
    return redirect('dashboard:dashboard_product')

  context = {
    'produk': produk
  }
  return render(request, 'dashboard/product_delete.html', context)

@login_required
def product_update(request, pk):
  produk = Produk.objects.get(id=pk)

  if request.method == 'POST':
    produk_form = ProdukCreationForm(request.POST, instance=produk)
    if produk_form.is_valid():
      produk_form.save()
      return redirect('dashboard:dashboard_product')
  else:
    produk_form = ProdukCreationForm(instance=produk)

  context = {
    'produk_form': produk_form,
    'produk': produk
  }

  return render(request, 'dashboard/product_update.html', context)

@login_required
def order(request):
  pesanan = Pemesanan.objects.all()
  total_staff = user_models.User.objects.all().count()
  total_product = Produk.objects.all().count()
  total_order = Pemesanan.objects.all().count()

  context = {
    'pesanans': pesanan,
    'total_staff': total_staff,
    'total_product': total_product,
    'total_order': total_order,
  }
  return render(request, 'dashboard/order.html', context)
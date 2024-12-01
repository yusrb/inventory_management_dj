from django.db import models
from django.contrib.auth.models import User

class Kategori(models.Model):
  nama_kategori = models.CharField(max_length=60)

  class Meta:
    verbose_name = "Kategori"
    verbose_name_plural = "Kategori"

  def __str__(self):
    return self.nama_kategori

class Produk(models.Model):
  nama = models.CharField(max_length=60)
  kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
  kuantitas = models.PositiveIntegerField()

  class Meta:
    verbose_name = "Produk"
    verbose_name_plural = "Produk"

  def __str__(self):
    return f"{self.nama} - {self.kuantitas}"

class Pemesanan(models.Model):
  produk = models.ForeignKey(Produk, on_delete=models.CASCADE,)
  staff = models.ForeignKey(User, on_delete=models.CASCADE)
  pemesanan_kuantitas = models.PositiveIntegerField()
  tgl_pemesanan = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = "Pemesanan"
    verbose_name_plural = "Pemesanan"

  def __str__(self):
    return f"{self.produk} diorder oleh {self.staff.username}"
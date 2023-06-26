from django.db import models

class Category(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    image = models.ImageField(("Kategori Resmi"), upload_to="category",max_length=200)

    def __str__(self):
        return self.title


class Card(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    title= models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik"))
    image = models.ImageField(("Kategori Resmi"), upload_to="category",max_length=200)
    date_now = models.DateField(("Tarih"), auto_now_add=False)
    price = models.FloatField((" Fiyat"))
    isactive = models.BooleanField(("Aktiflik"))
    new =models.BooleanField(("Yeni ürün"),default=True)
    def __str__(self):
        return self.title
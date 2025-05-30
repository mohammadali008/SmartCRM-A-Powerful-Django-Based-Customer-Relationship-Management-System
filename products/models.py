from django.db.models import Q
from django.db import models
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


# Create your models here.

# class Customer(models.Manager):
#     def get_active_products(self):
#         return self.get_queryset().filter(active=True)
#
#     def get_products_by_category(self, category_name):
#         return self.get_queryset().filter(categories__name__iexact=category_name, active=True)
#
#     def get_by_id(self, product_id):
#         qs = self.get_queryset().filter(id=product_id)
#         if qs.count() == 1:
#             return qs.first()
#         else:
#             return None
#
#     def search(self, query):
#         lookup = (
#                 Q(title__icontains=query) |
#                 Q(description__icontains=query) |
#                 Q(tag__title__icontains=query)
#         )
#         return self.get_queryset().filter(lookup, active=True).distinct()


class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name='نام محصول')
    price = models.IntegerField(verbose_name='قیمت')


    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"



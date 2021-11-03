from django.db import models
from django.urls import reverse

class Phone(models.Model):
    phone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y%m%d', blank=True)
    release_date = models.DateField(blank=True)
    lte_exists = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})

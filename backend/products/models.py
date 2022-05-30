from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,default=99.99)
    class Meta:
        db_table = "products"
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.08)

    def get_discount(self):
        return "122 testing"
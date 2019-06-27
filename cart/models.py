from django.db import models
from product.models import Product
from user.models import CustomerUser


class Cart(models.Model):
	user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username

class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.FloatField(default=0)

	def __str__(self):
		return self.item.title

	def getOwner(self):
		return self.cart.user.username

	def total(self):
		totals = self.quantity * self.item.price
		return totals;
        

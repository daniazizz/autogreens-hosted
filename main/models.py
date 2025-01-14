from django.db import models
from django.contrib.auth.models import AbstractUser

# User model
class User(AbstractUser):
    MARKET = 'MARKET'
    EXPRESS = 'EXPRESS'

    STORE_TYPE_CHOICES = [
        (MARKET, 'Market'),
        (EXPRESS, 'Express'),
    ]

    store_type = models.CharField(
        max_length=7,  # Max length of the longest choice ('EXPRESS')
        choices=STORE_TYPE_CHOICES,
        null=True,
        blank=True,
        help_text="Type of store: MARKET or EXPRESS."
    )
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    gy_reduction = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    
    # To resolve the conflicts, specify a unique related_name for the groups and user_permissions fields in 
    # your custom user model. This ensures that the reverse relationships are explicitly defined 
    # and do not clash with the default auth.User.
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

# Product model
class Product(models.Model):
    name_nl = models.CharField(max_length=255)
    name_fr = models.CharField(max_length=255)
    mc_ref = models.CharField(max_length=255, null=True, blank=True)
    gy_ref = models.CharField(max_length=255, null=True, blank=True)
    exp_sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    mk_sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    ref_correct = models.BooleanField(default=True)
    mk_promo = models.BooleanField(default=False)
    exp_promo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name_nl

# ProductPrice model
class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store_type = models.CharField(max_length= 7, choices=User.STORE_TYPE_CHOICES)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name_nl} - {self.price}"

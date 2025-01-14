from django.contrib import admin

# register all models in admin:

from .models import User, Product, ProductPrice

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name_nl',        # Display name in Dutch
        'name_fr',        # Display name in French
        'mc_ref',         # Display MC reference
        'gy_ref',         # Display GY reference
        'exp_sell_price', # Display expected sell price
        'mk_sell_price',  # Display market sell price
        'ref_correct',      # Display reference error status
    )
    list_filter = ('ref_correct',)  # Optional: Filter by reference error
    search_fields = ('name_nl', 'name_fr', 'mc_ref', 'gy_ref')  # Optional: Search functionality


admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPrice)


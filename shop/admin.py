from django.contrib import admin
from .models import Category, Organization, Event, Pricing_plan

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name', )}

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'address', 
                    'city', 'zip_code', 
                    'created_at', 'updated_at']
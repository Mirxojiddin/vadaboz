from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Province, District, City, CustomUser

# Register Province model with the admin
@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


# Register City model with the admin
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'province', 'district')
    list_filter = ('province', 'district')
    search_fields = ('name',)
    ordering = ('name',)


# Customize CustomUser model admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'province', 'district', 'city', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'province', 'district', 'city')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    # Fields to be displayed in the add/edit form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'name')}),
        ('Location', {'fields': ('province', 'district', 'city')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to be displayed in the create form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'name', 'province', 'district', 'city', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
        ),
    )

    # Fields to be used in the filter sidebar
    filter_horizontal = ('groups', 'user_permissions')


# Register the custom user admin class
admin.site.register(CustomUser, CustomUserAdmin)


class CityInline(admin.TabularInline):
    model = City
    extra = 1


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province')
    list_filter = ('province',)
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [CityInline]


admin.site.register(District, DistrictAdmin)
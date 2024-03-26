from django.contrib import admin

from .models import Menu, MenuItem


EMPTY_VALUE_DISPLAY = '- пусто -'


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_editable = ('name',)
    ordering = ('name',)
    search_fields = ('name__icontains',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'name', 'parent', 'url')
    list_editable = ('name', 'parent', 'url')
    search_fields = ('name__icontains',
                     'parent__name__icontains',
                     'menu__name__icontains',
                     'url__icontains')
    empty_value_display = EMPTY_VALUE_DISPLAY

    def full_name(self, obj: MenuItem) -> str:
        return str(obj)

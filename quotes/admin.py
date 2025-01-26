from django.contrib import admin

from .models import Quote

admin.site.register(Quote)

# Register your models here.
# @admin.register(Quote)
# class QuoteAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('email', 'first_name', 'last_name', 'is_staff', 'role')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
#         ('Important Dates', {'fields': ('last_login', 'date_joined')}),
#         ('Additional Info', {'fields': ('role',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active', 'role')}
#         ),
#     )
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)

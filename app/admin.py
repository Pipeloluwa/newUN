from django.contrib import admin

# Register your models here.
from .models import Information

class t1(admin.ModelAdmin):
    list_display = ("fullname", "phone_no", "instgram_handler", "email_address", "business_idea_craft_skill","description",)
    list_filter = ("fullname","email_address")

admin.site.register(Information,t1)
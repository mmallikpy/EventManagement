from django.contrib import admin

# Register your models here.
from .models import Ppicture, eventModel, BookedUser, EventCatorogy
class ModelAdmin(admin.ModelAdmin):
    list_display = ("p_image", "user",)
admin.site.register(Ppicture, ModelAdmin)

class eventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'event_location', 'event_descriptions', 'get_users',)
    
    def get_users(self, obj):
        return ", ".join([user.username for user in obj.user.all()])
    get_users.short_description = 'Users'

admin.site.register(eventModel, eventAdmin)



class bookAdmin(admin.ModelAdmin):
    list_display = ('book_status', 'event_data', 'user', )
    
admin.site.register(BookedUser, bookAdmin)


class eventCat(admin.ModelAdmin):
    list_display = ('catName',)
admin.site.register(EventCatorogy, eventCat)
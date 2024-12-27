from django.contrib import admin
from .models import Transportation,Flight,Train,Bus
# Register your models here.

admin.site.register(Transportation)
admin.site.register(Flight)
admin.site.register(Train)
admin.site.register(Bus)
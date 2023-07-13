from django.contrib import admin
from .models import Football
from .models import Baseball
from .models import Basketball
from .models import Hockey
from .models import Mma
from .models import Soccer

admin.site.register(Football)
admin.site.register(Baseball)
admin.site.register(Basketball)
admin.site.register(Hockey)
admin.site.register(Mma)
admin.site.register(Soccer)

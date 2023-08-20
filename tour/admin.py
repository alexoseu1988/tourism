from django.contrib import admin

from .models import Tour, Day, Inclusive, NotInclusive, ImageForDay, Icon, Review, WhyWe, Client

admin.site.register(Tour)
admin.site.register(Day)
admin.site.register(Inclusive)
admin.site.register(NotInclusive)
admin.site.register(ImageForDay)
admin.site.register(Icon)
admin.site.register(Review)
admin.site.register(WhyWe)
admin.site.register(Client)


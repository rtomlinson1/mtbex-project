from django.contrib import admin

from .models import blog, review, rating

admin.site.register(blog)
admin.site.register(review)
admin.site.register(rating)


from django.contrib import admin
from .models import Post, Comment #Reply

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "user", "date", )
    list_filter = ("date", )
    search_field = ["title", "body"]
    prepopulated_field = {"slug": ('title')}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "text")
    list_filter = ("active",)
    search_field = ["name", "created_on"]
    actions = ["approve"]

    def approve(self, request, queryset):
        queryset.update(active = True)


'''class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("subject", "email")
    list_filter =("date",)
    search_field = ["subject", "email"]
admin.site.register(Feedback, FeedbackAdmin)'''

admin.site.register(Post,PostAdmin,)
admin.site.register(Comment)
#admin.site.register(Reply)

from django.contrib import admin
from .models import Album, Media


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published", "created_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "media_type", "album", "title", "is_published", "created_at")
    list_filter = ("media_type", "is_published", "created_at", "album")
    search_fields = ("title", "caption", "video_url")

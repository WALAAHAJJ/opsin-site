from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="albums/covers/", blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class Media(models.Model):
    PHOTO = "photo"
    VIDEO = "video"
    MEDIA_TYPE_CHOICES = [
        (PHOTO, "Photo"),
        (VIDEO, "Video"),
    ]

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="media_items")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default=PHOTO)

    title = models.CharField(max_length=160, blank=True)
    caption = models.TextField(blank=True)

    image_file = models.ImageField(upload_to="portfolio/photos/", blank=True, null=True)
    video_url = models.URLField(blank=True)

    shot_date = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title or f"{self.media_type} #{self.pk}"

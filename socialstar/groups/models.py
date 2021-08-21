import misaka
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True,)
    description_html = models.TextField(editable=False, blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', default=1, on_delete=CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', default=1, on_delete=CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')

from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_recetas/')
    creado_en = models.DateTimeField(auto_now_add=True)
    autor = autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.titulo
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    bio = models.TextField(blank=True, null=True)  # Optional field for user bio

    def __str__(self):
        return f"{self.user.username}'s Profile"

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

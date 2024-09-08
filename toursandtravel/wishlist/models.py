from django.db import models

# Create your models here.
from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from packages.models import *


class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userwishlist', null=True, blank=True)

    def __str__(self):
        return self.user.name

    class Meta:
        ordering = ['-created_at']



class WishlistPackages(BaseModel):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishlistpackages', null=True, blank=True)
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='wishlistpackages', null=True, blank=True)

    def __str__(self):
        return self.package.name

    class Meta:
        ordering = ['-created_at']
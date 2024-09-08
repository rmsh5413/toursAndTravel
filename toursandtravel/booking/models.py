from django.db import models

# Create your models here.
from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from packages.models import *


class Booking(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userbookings', null=True, blank=True)
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='bookings', null=True, blank=True)
    adult = models.PositiveIntegerField()
    child = models.PositiveIntegerField()
    infant = models.PositiveIntegerField()
    booking_date = models.DateField()
    arrival_date = models.DateField()
    departure_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-created_at']


class AdultInformation(BaseModel):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='adults', null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
 

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['-created_at']


class ChildInformation(BaseModel):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
 

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['-created_at']


class InfantInformation(BaseModel):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='infants', null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
 

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['-created_at']


class Payment(BaseModel):
    PAYMENT_CHOICES = [('credit', 'Credit'),('card', 'Card')]

    PAYMENT_STATUS_CHOICES = [('Pending', 'Pending'),
                            ('Confirm','Confirm'),
                            ('Cancelled', 'Cancelled')
                         
                            ]
    payment_status = models.CharField(max_length = 50, choices = PAYMENT_STATUS_CHOICES, default="pending")
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments', null=True, blank=True)
    payment_method = models.CharField(max_length = 50, choices = PAYMENT_CHOICES, default="credit")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255)
    is_paid = models.BooleanField(default=False)


    def __str__(self):
        return self.booking.user.name
    
    class Meta:
        ordering = ['-created_at']
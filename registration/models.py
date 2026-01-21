

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password

# Custom validator for password rules
def validate_password(value):
    if not isinstance(value, str):
        raise ValidationError("Invalid password format.")
    if len(value) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if '@' not in value:
        raise ValidationError("Password must contain the '@' character.")

class UserRegistration(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Mobile number must be 10 digits")]
    )
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    
    password = models.CharField(
        max_length=128,
        validators=[validate_password]
    )

   
    hashed_password = models.CharField(max_length=255, null=True, blank=True)

    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        
        if self.password and not self.password.startswith("pbkdf2_sha256$"):
            self.hashed_password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

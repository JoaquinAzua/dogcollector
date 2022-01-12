from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f"({self.id}) - {self.name}"


# dogs = [
#     Dog('Luna', 'Pomeranian', 'Energetic innocent pup', 4),
#     Dog('Coco', 'Poodle', 'Serious but loving', 3),
#     Dog('Jackson', 'Labrador', 'Strong old soul', 7),
#     Dog('Molly', 'Labrador', 'Aggressively protective', 7),
# ]
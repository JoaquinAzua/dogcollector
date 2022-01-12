from django.db import models

# Create your models here.

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age



dogs = [
    Dog('Luna', 'Pomeranian', 'Energetic innocent pup', 4),
    Dog('Coco', 'Poodle', 'Serious but loving', 3),
    Dog('Jackson', 'Labrador', 'Strong old soul', 7),
    Dog('Molly', 'Labrador', 'Aggressively protective', 7),
]
from django.db import models

class CoalMine(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    total_coal_extracted = models.FloatField(help_text="Total coal extracted in tonnes per year")
    emission_factor = models.FloatField(help_text="Emission factor in tonnes CO2 per tonne of coal")

    def __str__(self):
        return self.name

    def calculate_emissions(self):
        return self.total_coal_extracted * self.emission_factor


class Tree(models.Model):
    name = models.CharField(max_length=100)
    carbon_absorption_rate = models.FloatField(help_text="Carbon absorption rate in tonnes per year")

    def __str__(self):
        return self.name

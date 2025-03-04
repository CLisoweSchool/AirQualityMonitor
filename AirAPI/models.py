from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    co2 = models.FloatField()
    humidity = models.FloatField()
    pm1_0 = models.FloatField(null=True, blank=True)
    pm2_5 = models.FloatField(null=True, blank=True)
    pm10_0 = models.FloatField(null=True, blank=True)
    temperature = models.FloatField()

    def __str__(self):
        return f"CO2: {self.co2} ppm at {self.timestamp}"
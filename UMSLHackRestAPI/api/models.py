from django.db import models
import datetime


def year_choices():
    return [(r,r) for r in range(2017, datetime.date.today().year+10)]


def current_year():
    return datetime.date.today().year


class MLRequest(models.Model):
    start_year = models.IntegerField(default=2017)
    end_year = models.IntegerField(default=2020)
    state = models.CharField(max_length=100)
    factor = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class Prediction(models.Model):
    request = models.ForeignKey(MLRequest, related_name='predictions', on_delete=models.CASCADE)
    #state = models.CharField(max_length=100)
    year = models.IntegerField()
    pollution = models.DecimalField(decimal_places=2, max_digits=32)
    #factor = models.CharField(max_length=50)

    def __str__(self):
        return f"Pollution Level: {self.pollution}\n" \
               f"Year: {self.year}"



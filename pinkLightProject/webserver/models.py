from django.db import models

# Create your models here.
class Train(models.Model):
    train_no = models.CharField(max_length=10)
    slot_no = models.CharField(max_length=10)
    seat_no = models.CharField(max_length=10)
    empty = models.BooleanField()

    def __str__(self):
        return f'[{self.train_no}] {self.seat_no} 번칸 {self.seat_no} : 사용여부: {self.empty}'



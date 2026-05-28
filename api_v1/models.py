from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(max_length=100)
    seats = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField()
    genre = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} - {self.time}"


class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seat_number = models.IntegerField()

    def __str__(self):
        return f"{self.customer.name} - seat {self.seat_number}"
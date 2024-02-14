from django.db import models


class Todo(models.Model):  # This creating a db table
    title = models.CharField(max_length=200)  # Columns
    status = models.BooleanField(default=False)  # Columns

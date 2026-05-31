
from django.db import models

from django.utils import timezone

from datetime import timedelta


# BOOK MODEL

class Book(models.Model):

    STATUS_CHOICES = [

        ('Available', 'Available'),

        ('Issued', 'Issued'),
    ]

    title = models.CharField(
        max_length=100
    )

    author = models.CharField(
        max_length=100
    )

    price = models.IntegerField()

    image = models.ImageField(
        upload_to='books/'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    def __str__(self):

        return self.title


# STUDENT MODEL

class Student(models.Model):

    name = models.CharField(
        max_length=100
    )

    department = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=15
    )

    address = models.TextField()

    profile_image = models.ImageField(
        upload_to='students/',
        null=True,
        blank=True
    )

    def __str__(self):

        return self.name


# BOOK ISSUE MODEL

class BookIssue(models.Model):

    token_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    issue_date = models.DateField(
        auto_now_add=True
    )

    expected_return_date = models.DateField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):

        if not self.token_number:

            last_id = BookIssue.objects.count() + 1

            self.token_number = f"LIB{1000 + last_id}"

        if not self.expected_return_date:

            self.expected_return_date = (

                timezone.now().date()

                + timedelta(days=20)
            )

        self.book.status = 'Issued'

        self.book.save()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.token_number


# BOOK RETURN MODEL

class BookReturn(models.Model):

    issue = models.OneToOneField(

        BookIssue,

        on_delete=models.CASCADE
    )

    return_date = models.DateField()

    fine_amount = models.IntegerField(

        default=0
    )

    def save(self, *args, **kwargs):

        late_days = (

            self.return_date -

            self.issue.expected_return_date

        ).days

        if late_days > 0:

            self.fine_amount = late_days * 2

        else:

            self.fine_amount = 0

        self.issue.book.status = 'Available'

        self.issue.book.save()

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.issue.token_number} Returned"



from django.shortcuts import render

from .models import (
    Book,
    Student,
    BookIssue,
    BookReturn
)


def home(request):

    total_books = Book.objects.count()

    total_students = Student.objects.count()

    books_issued = BookIssue.objects.count()

    books_returned = BookReturn.objects.count()

    recent_issues = BookIssue.objects.order_by(
        '-id'
    )[:5]

    context = {

        'total_books': total_books,

        'total_students': total_students,

        'books_issued': books_issued,

        'books_returned': books_returned,

        'recent_issues': recent_issues,
    }

    return render(request, 'home.html', context)


def books(request):

    books = Book.objects.all()

    return render(request, 'books.html', {

        'books': books
    })


def students(request):

    students = Student.objects.all()

    return render(request, 'students.html', {

        'students': students
    })


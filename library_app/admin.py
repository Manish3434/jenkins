
from django.contrib import admin

from .models import (
    Book,
    Student,
    BookIssue,
    BookReturn
)


# BOOK ADMIN

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author',
        'price',
        'status'
    )

    search_fields = (
        'title',
        'author'
    )

    actions_on_top = True

    actions_on_bottom = True


# STUDENT ADMIN

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'department',
        'phone'
    )

    search_fields = (
        'name',
        'department'
    )

    actions_on_top = True

    actions_on_bottom = True


# BOOK ISSUE ADMIN

@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):

    list_display = (
        'token_number',
        'student',
        'book',
        'issue_date',
        'expected_return_date'
    )

    search_fields = (
        'token_number',
        'student__name'
    )

    readonly_fields = (
        'token_number',
    )

    actions_on_top = True

    actions_on_bottom = True


# BOOK RETURN ADMIN

@admin.register(BookReturn)
class BookReturnAdmin(admin.ModelAdmin):

    list_display = (
        'issue',
        'return_date',
        'fine_amount'
    )

    readonly_fields = (
        'fine_amount',
    )

    actions_on_top = True

    actions_on_bottom = True


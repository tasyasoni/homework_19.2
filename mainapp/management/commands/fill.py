from django.core.management import BaseCommand
from mainapp.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_list = [
            {'first_name':'Иванов', 'last_name': 'Иван'},
            {'first_name': 'Петров', 'last_name':'Петр'},
            {'first_name': 'Семенов', 'last_name': 'Семен'},
            {'first_name': 'Александров', 'last_name': 'Александр'},
            {'first_name': 'Сонин', 'last_name': 'Сон'}
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        students_for_create = []
        for student_item in student_list:
            students_for_create.append(Student(**student_item))

        Student.objects.bulk_create(students_for_create)

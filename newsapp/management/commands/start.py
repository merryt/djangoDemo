import os
from django.core.management.base import BaseCommand, CommandError
args = 'TAKES NO ARGUMENT'


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Hello World!")
        os.system("source djangoDemo/bin/activate")
        os.system("pip3 install -r requirements.txt")
        os.system("python3 manage.py runserver")
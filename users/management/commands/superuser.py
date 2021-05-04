from django.core.management.base import BaseCommand
import django
from django.db import IntegrityError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Create Super User with username admin and password admin"

    def handle(self, *args, **kwargs):
        try:
            User.objects.create_superuser(username='admin',password="admin")
            self.stdout.write(self.style.SUCCESS('superuser created'))
        except IntegrityError:
            self.stdout.write(self.style.ERROR('"admin" user already created...'))
        except django.db.utils.OperationalError:
            self.stdout.write(self.style.ERROR('No table found...run command "make migrate" (OR) "python manage.py migrate"'))

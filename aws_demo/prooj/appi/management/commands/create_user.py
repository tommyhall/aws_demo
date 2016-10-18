from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create_user(
            username="tom",
            email="email@email.com",
            first_name="Tom",
            last_name="Hall"
        )
        user.set_password("password")
        user.save()

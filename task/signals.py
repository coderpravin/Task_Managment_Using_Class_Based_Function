from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def user_logged_in(sender, request, user, **kwargs):
    print("User loggin in ", user.username)

    
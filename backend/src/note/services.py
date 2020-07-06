from .models import User


def get_user_by_email(email):
    """
    """
    return User.objects.get_active().filter(email=email).first()

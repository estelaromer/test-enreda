from .models import User


def get_user_by_email(email):
    """
    Returns the User object with email the one 
    passed as argument, None if not found.
    """
    return User.objects.get_active().filter(email=email).first()

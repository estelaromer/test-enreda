from .models import User


def get_user_by_id(id):
    """
    """
    return User.objects.get_active().filter(id=id).first()

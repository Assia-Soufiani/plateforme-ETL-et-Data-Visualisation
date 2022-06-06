from graphene import Mutation, ObjectType, List, Field, Int, String, ID
from graphene_django.types import DjangoObjectType
from .models import CustomUser as User
class UserType(DjangoObjectType):
    """
    User model's fields are automatically mapped onto the UserType.
    """
    class Meta:
        """
        User model is configured here.
        Set fields you wish to be outputted.
        """
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'last_login',
            'email',
            'occupation',
            'company',
            'profile_title',
            'profile_description',
            'date_joined',
        )
class Query(object):
    """
    User queries.
    """
    users = List(UserType)
    user = Field(UserType, id=Int())
    @staticmethod
    def resolve_users(self, info, **kwargs):
        """
        Resolves all users.
        """
        return User.objects.all()
    @staticmethod
    def resolve_user(self, info, **kwargs):
        """
        Resolves a single user by ID.
        """
        return User.objects.get_by_id(**kwargs)
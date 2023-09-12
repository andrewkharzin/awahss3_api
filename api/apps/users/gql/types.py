import strawberry
from django.utils.translation import gettext_lazy as _
from apps.users.models import User  # Import your User model here

@strawberry.django.type(User)
class UserType:
    username: str
    email: str
    is_staff: bool
    is_active: bool
    date_joined: str  # Assuming you want the date as a string

    # # Additional fields for the 'role' property
    # is_new: bool
    # is_agent: bool
    # is_account: bool
    # is_shiftleader: bool
    # is_manager: bool

    # class Roles:
    #     NOT_AUTHORIZED: str
    #     AGENT: str
    #     ACCOUNT: str
    #     SHIFTLEADER: str
    #     MANAGER: str

    # role: Roles

    @strawberry.field
    def get_full_name(self) -> str:
        return f"{self.username} ({self.email})"

    @strawberry.field
    def get_short_name(self) -> str:
        return self.username

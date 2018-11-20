from .api import api

from .resources.user import UserResource, UsersResource

from .resources.auth.access_token import AccessTokenResource
from .resources.auth.password_reset_token import PasswordResetTokenResource


def apply_routes(bp):
    # Apply the RESTFul extension.
    api.init_app(bp)

    # Add the User resources.
    api.add_resource(UserResource, '/user/<string:id>')
    api.add_resource(UsersResource, '/user', '/user/')

    # Add the Auth resources.
    api.add_resource(AccessTokenResource, '/auth/access-token')
    api.add_resource(PasswordResetTokenResource, '/auth/password-reset-token')

from .api import api
from .resources.todo import TodosResource


def apply_routes(bp):
    # Apply the RESTFul extension.
    api.init_app(bp)

    # Add the Todo resources.
    api.add_resource(TodosResource, '/todo', '/todo/')

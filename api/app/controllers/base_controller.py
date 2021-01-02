from starlette.requests import Request

# Dependency
def get_db(request: Request):
    return request.state.db

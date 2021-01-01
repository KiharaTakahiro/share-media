from starlette.requests import Request

def get_connection(request: Request):
    return request.state.connection


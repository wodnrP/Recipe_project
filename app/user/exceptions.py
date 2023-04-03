from rest_framework.views import exception_handler

# 403 error code <-> 401 error code로 변환
def status_code_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.status_code == 403:
        response.status_code = 401
    
    return response
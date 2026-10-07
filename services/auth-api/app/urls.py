from django.conf import settings
from django.http import HttpRequest, JsonResponse
from django.urls import include, path
from functools import wraps
from django.views.decorators.http import require_GET

# from app.services.access_token import AccessTokenService
# from app.models.access_token import AccessToken
from shared.http.action_response import ActionResponse
# from shared.http.error_response import ErrorResponse

# def protected_route(view_func):
#     @wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         access_token_service = AccessTokenService()
#         user = access_token_service.verify_access_token(request)
#         if not user:
#             return JsonResponse({"error": "Unauthorized"}, status=401)

#         request.auth_user = user
#         return view_func(request, *args, **kwargs)
#     return wrapper

@require_GET
def health(request: HttpRequest) -> JsonResponse:
    return ActionResponse("auth-api", "health", "", "OK").to_json()
    

# @require_GET
# def token(request: HttpRequest) -> JsonResponse:    
#     print(f"setting: {settings}")
#     output = None
#     errors = []

#     try:
#         access_token_service = AccessTokenService()
#         output = access_token_service.get_access_token(
#             AccessToken(
#                 token_url=settings.TOKEN_URL,
#                 client_id=settings.CLIENT_ID,
#                 client_secret=settings.CLIENT_SECRET,
#                 scope=settings.SCOPE,
#                 grant_type=settings.GRANT_TYPE
#             )
#         )
#     except Exception as e:
#         errors = [ErrorResponse("ERR_ACCESS_TOKEN", "Error obtaining access token", e)]

#     success = output is not None and len(errors) == 0
    
#     return ActionResponse(service="auth-api|access_token", success=success, data=output, errors=errors).to_json()


# @protected_route
# def protected_route(request: HttpRequest) -> JsonResponse:    
#     user = request.auth_user
#     print(f"Access granted for user: {user}")
#     return JsonResponse({"message": "Access granted", "user": user})


auth_urlpatterns = [
    path("health", health, name="health"),
    # path("token", token, name="token"),
    # path("protected", protected_route, name="protected"),
]

urlpatterns = [
    path("api/v1/auth/", include(auth_urlpatterns)),
]

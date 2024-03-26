from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('Task.Api.v1.task.urls')),
    path('api/v1/authenticate/', include('Task.Api.v1.user_authentication.urls'))
]

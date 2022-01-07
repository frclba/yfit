"""undercard_18898 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

urlpatterns = [
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path("api/v1/", include("home.api.v1.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("rest-auth/", include("rest_auth.urls")),
    path("subscriptions/", include("subscriptions.urls")),
    # Override email confirm to use allauth's HTML view instead of rest_auth's API view
    path("rest-auth/registration/account-confirm-email/<str:key>/", confirm_email),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("api/v1/", include("dating.api.v1.urls")),
    path("dating/", include("dating.urls")),
    path("home/", include("home.urls")),
]

admin.site.site_header = "Undercard"
admin.site.site_title = "Undercard Admin Portal"
admin.site.index_title = "Undercard Admin"

# swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Undercard API",
        default_version="v1",
        description="API documentation for Undercard App",
    ),
    public=True,
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs"),
    path("__debug__/", include(debug_toolbar.urls)),
]
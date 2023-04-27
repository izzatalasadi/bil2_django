
from django.contrib import admin
from django.urls import include, path  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route

    # ADD NEW Routes HERE
    path("", include("apps.home.urls")),
]

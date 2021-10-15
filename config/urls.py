import app.views
from django.urls import path

urlpatterns = [
    path("", app.views.root, name="root")
]

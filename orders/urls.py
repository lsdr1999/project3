from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login_view", views.login_view, name="login_view"),
    path("register", views.register, name="register"),
    path("menu", views.menu, name="menu"),
    path("order", views.order, name="order"),
    path("add/<str:category>/<str:name>/<str:price>", views.add, name="add"),
    # path("delete/<str:category>/<str:name>/<str:price>", views.delete, name="delete"),
    path("logout_view", views.logout_view, name="logout_view"),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

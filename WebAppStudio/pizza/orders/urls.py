from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("menu", views.menu, name="menu"),
    path("add/<str:category>/<str:name>/<str:price>", views.add_to_order, name="add_to_order"),
    path("shoppingcart", views.shoppingcart, name="shoppingcart"),
    path("place_order/<price>", views.place_order, name="place_order"),
    path("pick_toppings/<str:category>/<str:name>/<str:price>", views.pick_toppings, name="pick_toppings"),
    path("addcoupon", views.addcoupon, name="addcoupon")
]

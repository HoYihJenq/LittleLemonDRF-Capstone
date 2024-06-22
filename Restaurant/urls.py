from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import MenuItemsView, SingleMenuItemsView, BookingView

router = DefaultRouter()
router.register(r'bookings', BookingView, basename="bookings")

urlpatterns = [
    path('', include(router.urls)),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemsView.as_view())

]

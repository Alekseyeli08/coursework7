from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView,
                          HabitListAPIView, HabitRetrieveAPIView,
                          HabitUpdateAPIView, PublicListAPIView)

app_name = HabitsConfig.name


urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habits-list"),
    path("public", PublicListAPIView.as_view(), name="public-list"),
    path("detail/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits-detail"),
    path("create/", HabitCreateAPIView.as_view(), name="habits-create"),
    path("<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habits-delete"),
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits-update"),
]

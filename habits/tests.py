from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="alexey@mail.ru")
        self.habit = Habit.objects.create(
            user=self.user,
            place="дом",
            time="20:30:00",
            action="растяжка",
            nice_habit=True,
            periodicity="once_day",
            time_to_complete="00:02:00",
            sign_of_publicity=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrive(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)

    def test_habit_create(self):
        url = reverse("habits:habits-create")
        data = {
            "place": "Ресторан",
            "time": "19:30:00",
            "action": "Трапеза",
            "nice_habit": True,
            "periodicity": "once_day",
            "time_to_complete": "00:00:02",
            "sign_of_publicity": True,
            "last_time_mailing": "2024-11-11",
            "user": self.user.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse("habits:habits-update", args=(self.habit.pk,))
        data = {
            "place": "Дом",
            "time": "19:30:00",
            "action": "Трапеза",
            "nice_habit": True,
            "periodicity": "once_week",
            "time_to_complete": "00:00:02",
            "sign_of_publicity": True,
            "last_time_mailing": "2024-11-11",
            "user": self.user.pk,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("periodicity"), "once_week")
        self.assertEqual(data.get("action"), "Трапеза")

    def test_habit_delete(self):
        url = reverse("habits:habits-delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": "дом",
                    "time": "20:30:00",
                    "action": "растяжка",
                    "nice_habit": True,
                    "periodicity": "once_day",
                    "reward": None,
                    "time_to_complete": "00:02:00",
                    "sign_of_publicity": True,
                    "last_time_mailing": "2024-11-10",
                    "user": self.user.pk,
                    "associated_habit": None,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_piblic_list(self):
        url = reverse("habits:public-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

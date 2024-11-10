import datetime

from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    PERIODICITY_CHOICES = (("once_day", "раз в день"), ("once_weekf", "раз в неделю"))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    place = models.CharField(max_length=300, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=250, verbose_name="Действие")
    nice_habit = models.BooleanField(default=True, verbose_name="Приятная привычка")
    associated_habit = models.ForeignKey(
        "self", **NULLABLE, on_delete=models.SET_NULL, verbose_name="Связанная привычка"
    )
    periodicity = models.CharField(
        max_length=50,
        choices=PERIODICITY_CHOICES,
        default="once_day",
        verbose_name="Периодичность",
    )
    reward = models.CharField(**NULLABLE, max_length=300, verbose_name="Вознаграждение")
    time_to_complete = models.DurationField(verbose_name="Время на выполнение")
    sign_of_publicity = models.BooleanField(
        default=True, verbose_name="признак публичности"
    )
    last_time_mailing = models.DateField(
        **NULLABLE, default=datetime.date.today, verbose_name="время последней рассылки"
    )

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"

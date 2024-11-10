from datetime import timedelta

from rest_framework.serializers import ValidationError


class HabitsValidator:
    def __call__(self, value):
        """Валидация данных по тз"""
        val = dict(value)
        if val.get("nice_habit"):
            if value.get("associated_habit") or value.get("reward"):
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки или вознаграждения"
                )

        if not value.get("nice_habit"):
            if value.get("associated_habit") and value.get("reward"):
                raise ValidationError(
                    "Может быть связанная привычка или вознаграждение,"
                )

        if val.get("time_to_complete") > timedelta(minutes=2):
            raise ValidationError(
                "Время выполнения привычки не может быть больше 2-х минут!"
            )

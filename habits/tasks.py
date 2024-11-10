import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task()
def send_habit():
    habits = Habit.objects.filter(nice_habit=True)
    date_now = datetime.datetime.now().date()
    time_now = datetime.datetime.now().time()

    for habit in habits:
        if habit.last_time_mailing == date_now:
            user_tg_id = habit.user.tg_chat_id
            message = f"сегодня в {habit.time} нужно {habit.action} в {habit.place}"
            if habit.time > time_now and habit.periodicity == "once_day":
                habit.last_time_mailing += datetime.timedelta(days=1)
                send_telegram_message(user_tg_id, message)
                habit.save()
            elif habit.time > time_now and habit.periodicity == "once_week":
                habit.last_time_mailing += datetime.timedelta(days=7)
                send_telegram_message(user_tg_id, message)
                habit.save()

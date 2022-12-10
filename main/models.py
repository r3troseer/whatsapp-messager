import json
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django_celery_beat.models import IntervalSchedule, PeriodicTask, ClockedSchedule
from datetime import datetime, date, timedelta

# Create your models here.
# import pywhatkit
# from django.db.models.signals import post_save
# from django.dispatch import receiver
class TimeInterval(models.TextChoices):
    hour = "hours"
    minute = "minutes"
    day = "days"


class MessageStatus(models.TextChoices):
    active = "Active"
    disabled = "Disabled"


BOOL_CHOICES = ((True, "Yes"), (False, "No"))


class message(models.Model):
    message = models.CharField(max_length=1000)
    time = models.TimeField()
    date = models.DateField(default=date.today, null=True)
    wait_time = models.IntegerField(
        default=20,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(15),
        ],
        blank=True,
    )
    tab_close = models.BooleanField(default=False, null=True, choices=BOOL_CHOICES)
    close_time = models.IntegerField(
        null=True,
        blank=True,
    )
    interval = models.IntegerField(null=True, blank=True)
    interval_period = models.CharField(
        max_length=100, choices=TimeInterval.choices, null=True, blank=True
    )
    task = models.OneToOneField(
        PeriodicTask, on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.CharField(
        max_length=100, choices=MessageStatus.choices, null=True, blank=True
    )
    one_off = models.BooleanField(default=False, choices=BOOL_CHOICES)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        if self.task is not None:
            self.task.delete()

        return super(self.__class__, self).delete(*args, **kwargs)

    def setup_task(self, group_id=None, phone_no=None):
        if self.one_off == True:
            self.task = PeriodicTask.objects.create(
                name=str(self),
                task="direct_task",
                clocked=self.clocked_schedule,
                args=json.dumps(
                    [
                        self.message,
                        self.time.hour,
                        self.time.minute,
                        self.wait_time,
                        self.tab_close,
                        self.close_time,
                    ]
                ),
                kwargs=json.dumps(
                    {
                        "group_id": group_id,
                        "phone_no": phone_no,
                    }
                ),
                start_time=timezone.now(),
                one_off=self.one_off,
            )
        elif self.one_off == False:
            self.task = PeriodicTask.objects.create(
                name=str(self),
                task="direct_task",
                interval=self.interval_schedule,
                args=json.dumps(
                    [
                        self.message,
                        self.time.hour,
                        self.time.minute,
                        self.wait_time,
                        self.tab_close,
                        self.close_time,
                    ]
                ),
                kwargs=json.dumps(
                    {
                        "group_id": group_id,
                        "phone_no": phone_no,
                    }
                ),
                start_time=timezone.now(),
                one_off=self.one_off,
                last_run_at=timezone.now()
                - timedelta(**{self.interval_period: self.interval}),
            )
        self.save()

    @property
    def interval_schedule(self):
        if self.one_off == False:
            schedule, _ = IntervalSchedule.objects.get_or_create(
                every=self.interval, period=self.interval_period
            )
            return schedule
        else:
            return None

    @property
    def clocked_schedule(self):
        if self.one_off == True:
            date = self.date
            time = self.time
            clocked_time = datetime.combine(date, time) - timedelta(minutes=2)
            schedule, _ = ClockedSchedule.objects.get_or_create(
                clocked_time=clocked_time
            )
            return schedule
        else:
            return None

        # if self.time_interval == TimeInterval.five_mins:
        #     return IntervalSchedule.objects.get(every=5, period="minutes")
        # if self.time_interval == TimeInterval.one_hour:
        #     return IntervalSchedule.objects.get(every=1, period="hours")

        # raise NotImplementedError(
        #     """Interval Schedule for {interval} is not added.""".format(
        #         interval=self.time_interval.value
        #     )
        # )


class DirectMessage(message):
    phone_no = PhoneNumberField(blank=False)

    def __str__(self):
        return f"{self.message} sent to {self.phone_no} by {self.time}"


# @receiver(post_save, sender=DirectMessage)
# def send_message(sender, instance, *args, **kwargs):
#     print("initiated")
#     if instance:
#         phone_no = str(instance.phone_no)
#         message = instance.message
#         hour = instance.time.hour
#         minute = instance.time.minute
#         print(phone_no, message, hour, minute)

#         pywhatkit.sendwhatmsg(phone_no, message, hour, minute, 10)
#         print(f"message will be sent by {instance.time} ")


class GroupMessage(message):
    group_id = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.message} sent to {self.group_id} by {self.time}"

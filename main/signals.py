import pywhatkit
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import DirectMessage, GroupMessage, MessageStatus
from main.tasks import direct_task


@receiver(post_save, sender=GroupMessage)
@receiver(post_save, sender=DirectMessage)
def send_message(sender, instance, created, *args, **kwargs):
    print("initiated")
    if created:
        # if instance.interval and instance.interval_period:
            if sender == DirectMessage:
                print("direct")
                instance.setup_task(phone_no=str(instance.phone_no))
            elif sender == GroupMessage:
                instance.setup_task(group_id=instance.group_id)
    else:
        if instance.task is not None:
            instance.task.enabled = instance.status == MessageStatus.active
            instance.task.save()
    # phone_no = str(instance.phone_no)
    # message = instance.message
    # hour = instance.time.hour
    # minute = instance.time.minute
    # wait_time=instance.wait_time
    # tab_close=instance.tab_close
    # close_time=instance.close_time
    # date=instance.date
    # direct_task.apply_async(args=[phone_no, message, hour, minute, wait_time, tab_close, close_time], eta=date)
    # print("done")

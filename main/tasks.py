from celery import shared_task
import pywhatkit as pyw

# from main.models import DirectMessage, GroupMessage
@shared_task(name='direct_task')
def direct_task(
    message,
    hour,
    minute,
    wait_time,
    tab_close,
    close_time,
    phone_no=None,
    group_id=None,
):
    print("in progress")
    print(phone_no, message, hour, minute)
    if phone_no:
        pyw.sendwhatmsg(
            phone_no, message, hour, minute, wait_time, tab_close, close_time
        )
    elif group_id:
        pyw.sendwhatmsg_to_group(
            group_id, message, hour, minute, wait_time, tab_close, close_time
        )
    else:
        print('message not sent')


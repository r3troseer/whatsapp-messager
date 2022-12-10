import pywhatkit as pyw
from django.utils import timezone
from datetime import datetime, time, timedelta

# pywhatkit.sendwhatmsg("+2349095189314", "messagess", 15, 4, 30, None, None)
timezone.now
# print(time.now())
print(time(23, 59, 59) - timedelta(minutes=2))


# def direct_task(
#     message,
#     hour,
#     minute,
#     wait_time,
#     tab_close,
#     close_time,
#     phone_no=None,
#     group_id=None,
# ):
#     print("in progress")
#     print(phone_no, message, hour, minute)
#     if phone_no:
#         pyw.sendwhatmsg(
#             phone_no, message, hour, minute, wait_time, tab_close, close_time
#         )
#     elif group_id:
#         pyw.sendwhatmsg_to_group(
#             group_id, message, hour, minute, wait_time, tab_close, close_time
#         )
#     else:
#         print('message not sent')

# direct_task("test", 7, 51, 20, None, None, phone_no="+2349095189314")
# direct_task("test", 7, 47, 20, None, None, group_id="GEuIrZsW5JRK0NHuknyNn2")

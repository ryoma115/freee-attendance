from django.db import models
from django.contrib.auth import get_user_model

class SubmitAttendance(models.Model):

    class Meta:
        db_table = 'attendance'

    PLACES = (
        (1, 'オフィス'),
        (2, '自宅'),
        (3, 'コワーキングスペース'),
        (4, '出張先'),
        (5, 'その他'),
    )
    IN_OUT = (
        (0, '出勤'),
        (1, '退勤'),
        (2, '休憩 始'),
        (2, '休憩 終')
    )

    employee = models.ForeignKey(
      get_user_model(),
      verbose_name='社員名',
      on_delete=models.CASCADE,
      default=None
    )
    place = models.IntegerField(
      verbose_name='勤務先',
      choices=PLACES,
      default=None
    )
    in_out = models.IntegerField(
      verbose_name='出勤/退勤',
      choices=IN_OUT,
      default=None
    )
    remarks = models.TextField(
      verbose_name='備考欄',
      blank=True,
      null=True,
      max_length=300
    )
    time = models.TimeField(
      verbose_name='打刻時間'
    )
    date = models.DateField(
      verbose_name='打刻日'
    )

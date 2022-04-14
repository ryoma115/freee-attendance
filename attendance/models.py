from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
class SubmitAttendance(models.Model):

    class Meta:
        db_table = 'attendance'

    PLACES = (
        (0, 'オフィス'),
        (1, '自宅'),
        (2, 'コワーキングスペース'),
        (3, '出張先'),
        (4, 'その他'),
    )
    IN_OUT = (
        (0, '出勤'),
        (1, '退勤'),
        (2, '休憩 始'),
        (3, '休憩 終')
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

    in_out_dict = dict(IN_OUT)

    def __str__(self):
        return  str(User.objects.get(id=self.employee_id)) + ' : ' + str(self.in_out_dict[self.in_out])

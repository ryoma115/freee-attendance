from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SubmitAttendance
from .forms import SubmitAttendanceForm
from datetime import datetime
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        form = SubmitAttendanceForm
        context = {
            'form': form,
            "user": request.user,
        }
        return render(request, 'attendance/index.html', context)
index = IndexView.as_view()

class ResultView(LoginRequiredMixin, View):
    def post(self, request):
        form = SubmitAttendanceForm(request.POST)
        now = datetime.now()
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute

        obj = form.save(commit=False)
        obj.place = request.POST["place"]
        obj.in_out = request.POST["in_out"]
        obj.employee = request.user
        obj.remarks = request.POST["remarks"]
        obj.date = datetime.now().date()
        obj.time = datetime.now().time()
        obj.save()
        if request.POST["in_out"] == '1':
            comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "出勤確認しました。今日も頑張りましょう！"
        else:
            comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "退勤確認しました。お疲れ様でした！"
        context = {
            'place': SubmitAttendance.PLACES[int(obj.place)-1][1],
            'comment': comment,
        }
        return render(request, 'attendance/result.html', context)
result = ResultView.as_view()

class attendancesList(LoginRequiredMixin, generic.ListView):
  model = SubmitAttendance
  template_name = 'attendance/list.html'
  context_object_name = 'attendances'

attendancesList = attendancesList.as_view()


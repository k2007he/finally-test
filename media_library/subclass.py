from datetime import datetime
from .core import TodoItem

class DailySchedule(TodoItem):
    def __init__(self, date, time, title):
        super().__init__(title)
        if not date or not time:
            raise ValueError("날짜와 시간은 필수입니다.")
        self.date = date  # 예: "2026-06-20"
        self.time = time  # 예: "14:00"

    def get_summary(self):
        # 💡 현재 컴퓨터 시간과 일과의 예정 시간을 비교합니다.
        try:
            current_now = datetime.now()
            schedule_time = datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")
            
            # 예정 시간이 현재 시간보다 과거라면 자동으로 완료(True) 처리
            if schedule_time <= current_now:
                self.is_completed = True
        except ValueError:
            # 사용자가 날짜 형식을 잘못 입력했을 때 프로그램이 튕기지 않도록 예외 처리
            pass

        status = "☑" if self.is_completed else "☐"
        return f"{status} [{self.date} {self.time}] {self.title}"

    def get_time_info(self):
        return f"{self.date} {self.time}"


class Checklist(TodoItem):
    def __init__(self, title):
        super().__init__(title)

    def get_summary(self):
        status = "☑" if self.is_completed else "☐"
        return f"{status} {self.title}"

    def reset_status(self):
        self.is_completed = False
from .core import TodoItem


class DailySchedule(TodoItem):
    def __init__(self, date, time, title):
        super().__init__(title)
        if not date or not time:
            raise ValueError("날짜와 시간은 필수입니다.")
        self.date = date
        self.time = time

    def get_summary(self):
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

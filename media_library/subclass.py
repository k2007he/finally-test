from .core import TodoItem

class DailySchedule(TodoItem):
    """하루 일과 관리 클래스"""
    def __init__(self, date: str, time: str, title: str):
        super().__init__(title)
        if not date or not time:
            raise ValueError("날짜와 시간은 필수 항목입니다.")
        self.date = date
        self.time = time

    def get_summary(self) -> str:
        # 완료 여부에 따라 앞에 표시를 다르게 해줄 수도 있습니다 (현재는 정렬용으로 유지)
        status = "☑" if self.is_completed else "☐"
        return f"{status} [{self.date} {self.time}] {self.title}"

    def get_item_type(self) -> str:
        return "하루 일과"


class Checklist(TodoItem):
    """일정과 무관한 체크리스트 클래스"""
    def __init__(self, title: str):
        super().__init__(title)

    def get_summary(self) -> str:
        # 💡 완료되면 ☑, 미완료면 ☐ 기호가 붙습니다.
        icon = "☑" if self.is_completed else "☐"
        return f"{icon} {self.title}"

    def get_item_type(self) -> str:
        return "체크리스트"
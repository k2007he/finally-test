from datetime import datetime

class Task:
    """모든 할 일 항목의 부모 클래스"""
    def __init__(self, title):
        if not title or not title.strip():
            raise ValueError("제목은 비어있을 수 없습니다.")
        self.title = title
        self._is_completed = False

    def mark_as_completed(self):
        """할 일을 완료 상태로 변경한다."""
        self._is_completed = True

    def _get_status_mark(self):
        """완료 여부에 따른 표시를 반환하는 비공개 메서드"""
        return "[✔]" if self.is_completed else "[ ]"

    @property
    def is_completed(self):
        """완료 상태를 반환한다."""
        return self._is_completed

    def get_summary(self):
        """할 일의 요약 정보를 반환한다."""
        return self.title


class TodoItem(Task):
    """마감 시간을 가진 할 일 항목"""
    def __init__(self, title, deadline=None):
        super().__init__(title)
        self.deadline = deadline

    @property
    def is_completed(self):
        """
        수동 완료 여부 또는 마감 시간 경과 여부를 확인한다.
        
        >>> todo = TodoItem("과제", deadline=datetime(2020, 1, 1))
        >>> todo.is_completed
        True
        """
        if self._is_completed:
            return True
        if self.deadline and datetime.now() > self.deadline:
            return True
        return False

    def get_summary(self):
        """
        할 일 요약을 반환한다.
        
        :return: 요약 문자열
        """
        return f"{self._get_status_mark()} {self.title}"


class Checklist(Task):
    """단순 체크리스트 항목"""
    def __init__(self, title):
        super().__init__(title)

    def get_summary(self):
        """체크리스트 요약 반환"""
        return f"{self._get_status_mark()} {self.title}"
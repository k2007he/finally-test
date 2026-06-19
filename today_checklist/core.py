class TodoItem:
    """할 일 목록의 개별 항목을 관리하는 클래스

    :ivar title: 할 일의 제목
    :ivar deadline: 할 일의 마감 시간 (datetime 객체 또는 None)
    """

    def __init__(self, title, deadline=None):
        """TodoItem 인스턴스를 초기화합니다.

        :param title: 할 일의 제목 (비어있을 수 없음)
        :param deadline: 마감 시간 (기본값 None, 형식: datetime 객체)
        :raises ValueError: 제목이 없거나 공백만 있을 때 발생

        사용 예시:
        >>> from datetime import datetime
        >>> todo = TodoItem("파이썬 과제하기", deadline=datetime(2026, 12, 31, 23, 59))
        >>> todo.title
        '파이썬 과제하기'
        """
        self._check_title(title)
        self.title = title
        self.deadline = deadline
        self._is_completed = False

    def _check_title(self, title):
        """제목의 유효성을 검사합니다.

        :param title: 검사할 할 일 제목 문자열
        :raises ValueError: 제목이 없거나 공백만 있을 때 발생
        """
        if not title or title.strip() == "":
            raise ValueError("내용이 비어있을 수 없습니다.")

    @property
    def is_completed(self):
        """할 일의 완료 여부를 반환합니다. (시간 동기화 자동 체크 기능)

        :return: 완료 여부 (Boolean)
        """
        import datetime

        if self._is_completed:
            return True
        if self.deadline and datetime.datetime.now() > self.deadline:
            return True
        return self._is_completed

    @is_completed.setter
    def is_completed(self, value):
        """완료 상태를 수동으로 설정합니다."""
        self._is_completed = value

    def get_summary(self):
        """할 일의 제목 요약을 반환합니다.

        :return: 할 일 제목 문자열
        """
        return self.title

    def mark_as_completed(self):
        """할 일 상태를 완료(True)로 변경합니다."""
        self._is_completed = True

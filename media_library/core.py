class TodoItem:
    """일정 관리 시스템의 최상위 기반 클래스"""
    def __init__(self, title: str):
        self._validate_title(title) # 💡 비공개 메서드를 생성자에서 호출
        self.title = title
        self.is_completed = False

    def _validate_title(self, title: str):
        """내용이 비어있는지 검증하는 비공개 메서드"""
        if not title or not title.strip():
            raise ValueError("내용(title)은 비어있을 수 없습니다.")

    def get_summary(self) -> str:
        return self.title

    def mark_as_completed(self):
        """항목을 완료 상태로 변경합니다."""
        self.is_completed = True
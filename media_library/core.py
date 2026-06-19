class TodoItem:
    def __init__(self, title):
        self._check_title(title)
        self.title = title
        self.is_completed = False

    def _check_title(self, title):
        if not title or title.strip() == "":
            raise ValueError("내용이 비어있을 수 없습니다.")

    def get_summary(self):
        return self.title

    def mark_as_completed(self):
        self.is_completed = True
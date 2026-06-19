import pytest
from datetime import datetime, timedelta
from today_checklist.core import TodoItem, Checklist

# ==========================================
# 1. 정상 케이스 (5건 이상)
# ==========================================

def test_todo_creation_success():
    """정상 1: 객체 생성 및 속성 확인"""
    todo = TodoItem("파이썬 과제하기")
    assert todo.title == "파이썬 과제하기"
    assert todo.is_completed is False

def test_todo_initial_status():
    """정상 2: 초기 상태 확인"""
    todo = TodoItem("방 청소")
    assert todo.is_completed is False

def test_mark_as_completed():
    """정상 3: 수동 완료 처리"""
    todo = TodoItem("운동하기")
    todo.mark_as_completed()
    assert todo.is_completed is True

def test_get_summary():
    """정상 4: 요약 문자열 반환 확인"""
    todo = TodoItem("블로그 글 쓰기")
    assert "블로그 글 쓰기" in todo.get_summary()

def test_auto_complete_when_time_passed():
    """정상 5: 마감 시간 경과 시 자동 완료"""
    past_time = datetime.now() - timedelta(hours=1)
    todo = TodoItem("마감이 지난 과제", deadline=past_time)
    assert todo.is_completed is True

def test_not_completed_before_deadline():
    """정상 6: 마감 전 상태 확인"""
    future_time = datetime.now() + timedelta(hours=1)
    todo = TodoItem("마감이 남은 과제", deadline=future_time)
    assert todo.is_completed is False

# ==========================================
# 2. 엣지 케이스 (3건 이상)
# ==========================================

def test_error_when_title_is_none():
    """엣지 1: 제목 None 입력 시 에러"""
    with pytest.raises(ValueError):
        TodoItem(None)

def test_error_when_title_is_empty_string():
    """엣지 2: 제목 빈 문자열 입력 시 에러"""
    with pytest.raises(ValueError):
        TodoItem("")

def test_error_when_title_is_only_spaces():
    """엣지 3: 제목 공백 입력 시 에러"""
    with pytest.raises(ValueError):
        TodoItem("    ")
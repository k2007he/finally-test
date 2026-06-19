import pytest
from datetime import datetime, timedelta
from today_checklist.core import TodoItem

# ==========================================
# 1. 정상 케이스
# ==========================================

def test_todo_creation_success():
    """정상 케이스 1: 할 일 객체가 올바르게 생성되는지 확인"""
    todo = TodoItem("파이썬 과제하기")
    assert todo.title == "파이썬 과제하기"
    assert todo.is_completed is False


def test_todo_initial_status():
    """정상 케이스 2: 처음 생성된 할 일의 완료 상태는 항상 False인지 확인"""
    todo = TodoItem("방 청소")
    assert todo.is_completed is False


def test_mark_as_completed():
    """정상 케이스 3: mark_as_completed 호출 시 완료 상태가 True로 변하는지 확인"""
    todo = TodoItem("운동하기")
    todo.mark_as_completed()
    assert todo.is_completed is True


def test_get_summary():
    """정상 케이스 4: get_summary가 할 일의 제목을 정확히 반환하는지 확인"""
    todo = TodoItem("블로그 글 쓰기")
    assert todo.get_summary() == "블로그 글 쓰기"


def test_auto_complete_when_time_passed():
    """정상 케이스 5: 마감 시간이 지나면 자동으로 is_completed가 True가 되는지 확인"""
    # 현재 시간보다 1시간 전으로 마감 시간 설정
    past_time = datetime.now() - timedelta(hours=1)
    todo = TodoItem("마감이 지난 과제", deadline=past_time)
    
    # 수동으로 완료 처리를 안 했어도 자동으로 True가 되어야 함
    assert todo.is_completed is True


def test_not_completed_before_deadline():
    """정상 케이스 6: 마감 시간이 아직 안 지났다면 False를 유지하는지 확인"""
    # 현재 시간보다 1시간 뒤로 마감 시간 설정
    future_time = datetime.now() + timedelta(hours=1)
    todo = TodoItem("마감이 남은 과제", deadline=future_time)
    
    assert todo.is_completed is False


# ==========================================
# 2. 엣지 케이스
# ==========================================

def test_error_when_title_is_none():
    """엣지 케이스 1: 제목이 None일 때 ValueError가 발생하는지 확인"""
    with pytest.raises(ValueError):
        TodoItem(None)


def test_error_when_title_is_empty_string():
    """엣지 케이스 2: 제목이 빈 문자열("")일 때 ValueError가 발생하는지 확인"""
    with pytest.raises(ValueError):
        TodoItem("")


def test_error_when_title_is_only_spaces():
    """엣지 케이스 3: 제목이 공백으로만 이루어졌을 때("   ") ValueError가 발생하는지 확인"""
    with pytest.raises(ValueError):
        TodoItem("     ")
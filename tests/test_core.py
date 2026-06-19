import pytest
from today_checklist import TodoItem, DailySchedule, Checklist

# 1. 부모 클래스 기본 생성 테스트
def test_todo_item_creation():
    item = TodoItem("기본 할 일")
    assert item.title == "기본 할 일"
    assert item.is_completed is False

# 2. 부모 클래스 빈 값 입력시 예외 처리 테스트
def test_todo_item_empty_title():
    with pytest.raises(ValueError):
        TodoItem("")

# 3. 부모 클래스 완료 처리 기능 테스트
def test_todo_item_mark_completed():
    item = TodoItem("공부하기")
    item.mark_as_completed()
    assert item.is_completed is True

# 4. 하루 일과 클래스 생성 및 속성 테스트
def test_daily_schedule_creation():
    schedule = DailySchedule("2026-06-20", "14:00", "프로젝트 회의")
    assert schedule.date == "2026-06-20"
    assert schedule.time == "14:00"
    assert schedule.title == "프로젝트 회의"

# 5. 하루 일과 빈 값 예외 처리 테스트
def test_daily_schedule_empty_value():
    with pytest.raises(ValueError):
        DailySchedule("", "14:00", "오류 테스트")

# 6. 하루 일과 요약 문구 포맷 테스트
def test_daily_schedule_summary():
    schedule = DailySchedule("2026-06-20", "09:00", "출근")
    assert schedule.get_summary() == "☐ [2026-06-20 09:00] 출근"

# 7. 하루 일과 시간 정보 반환 테스트
def test_daily_schedule_time_info():
    schedule = DailySchedule("2026-06-20", "18:00", "저녁 약속")
    assert schedule.get_time_info() == "2026-06-20 18:00"

# 8. 체크리스트 클래스 요약 문구 포맷 테스트
def test_checklist_summary():
    chk = Checklist("마트 가기")
    assert chk.get_summary() == "☐ 마트 가기"

# 9. 체크리스트 상태 초기화 테스트
def test_checklist_reset_status():
    chk = Checklist("운동하기")
    chk.mark_as_completed()
    assert chk.is_completed is True
    chk.reset_status()
    assert chk.is_completed is False
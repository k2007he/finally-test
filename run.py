from today_checklist import DailySchedule, Checklist

def main():
    schedules = []
    checklists = []

    while True:                      #while True: 포로그램을 종료하기 전까지 계속 메뉴를 보여 주기 위해 무한루프를 돌림. '메인메뉴'와 '상세 메뉴' 분리       
        print("\n" + "=" * 40)
        print(" 📅 개인 일정 관리 시스템 📋")
        print("=" * 40)
        print("1. 하루 일과 관리")
        print("2. 체크리스트 관리")
        print("q. 프로그램 종료")
        
        main_choice = input("원하는 메뉴를 선택하세요 (1/2/q): ").strip().lower()

        # ----------------------------------------------------
        # 1. 하루 일과 관리 메뉴
        # ----------------------------------------------------
        if main_choice == "1":
            while True:
                print("\n[ 📅 하루 일과 관리 ]")
                print("1. 하루 일과 추가")
                print("2. 하루 일과 확인 (시간순 정렬)")
                print("3. 하루 일과 완료 처리")  # 새로 추가된 메뉴
                print("0. 메인 메뉴로 돌아가기")
                sub_choice = input("작업을 선택하세요 (1/2/3/0): ").strip()

                if sub_choice == "0":
                    break

                if sub_choice == "1":
                    print("\n--- 📝 하루 일과 추가 (뒤로 가려면 'q' 입력) ---")
                    date = input("날짜를 입력하세요 (예: 2026-06-20): ").strip()
                    if date.lower() == 'q': 
                        print("↩️ 입력을 취소하고 돌아갑니다.")
                        continue
                        
                    time = input("시간을 입력하세요 (예: 14:00): ").strip()
                    if time.lower() == 'q': 
                        print("↩️ 입력을 취소하고 돌아갑니다.")
                        continue
                        
                    title = input("일정 이름을 입력하세요: ").strip()
                    if title.lower() == 'q': 
                        print("↩️ 입력을 취소하고 돌아갑니다.")
                        continue
                    
                    try
                        new_schedule = DailySchedule(date=date, time=time, title=title)
                        schedules.append(new_schedule)
                        print("✅ 하루 일과가 성공적으로 추가되었습니다!")
                    except ValueError as e:
                        print(f"❌ 오류: {e}")    

                elif sub_choice == "2":
                    print("\n--- 👀 하루 일과 확인 (시간순) ---")
                    if not schedules:
                        print("등록된 하루 일과가 없습니다.")
                    else:
                        sorted_schedules = sorted(schedules, key=lambda x: (x.date, x.time))
                        for index, item in enumerate(sorted_schedules, 1):
                            print(f"{index}. {item.get_summary()}")

                #  새로 구현된 하루 일과 완료 처리 기능
                elif sub_choice == "3":
                    print("\n--- ✔️ 하루 일과 완료 처리 (뒤로 가려면 'q' 입력) ---")
                    if not schedules:
                        print("완료 처리할 하루 일과가 없습니다.")
                        continue
                    
                    for index, item in enumerate(schedules, 1):
                        print(f"{index}. {item.get_summary()}")
                    
                    user_input = input("완료할 항목의 번호를 입력하세요: ").strip()
                    if user_input.lower() == 'q':           #사용자 입력에서 불필요한 공백을 제거(strip)하고, 대문자를 소문자로 바꿔(lower) 입력값 오류를 줄였습니다.
                        print("↩️ 작업을 취소하고 돌아갑니다.") 
                        continue
                        
                    try:
                        num = int(user_input)
                        if 1 <= num <= len(schedules):
                            schedules[num - 1].mark_as_completed()
                            print(f"✅ '{schedules[num - 1].title}' 일과가 완료 처리되었습니다!")
                        else:
                            print("❌ 올바른 번호 범위가 아닙니다.")
                    except ValueError:
                        print("❌ 숫자 또는 'q'만 입력해 주세요.")
                else:
                    print("❌ 잘못된 선택입니다. 다시 입력해주세요.")

        # ----------------------------------------------------
        # 2. 체크리스트 관리 메뉴
        # ----------------------------------------------------
        elif main_choice == "2":
            while True:
                print("\n[ 📋 체크리스트 관리 ]")
                print("1. 체크리스트 추가")
                print("2. 체크리스트 확인 (완료 항목 상단 정렬)")
                print("3. 체크리스트 완료 처리")
                print("0. 메인 메뉴로 돌아가기")
                sub_choice = input("작업을 선택하세요 (1/2/3/0): ").strip()

                if sub_choice == "0":
                    break

                if sub_choice == "1":
                    print("\n--- 📝 체크리스트 추가 (뒤로 가려면 'q' 입력) ---")
                    title = input("해야 할 일을 입력하세요: ").strip()
                    if title.lower() == 'q':
                        print("↩️ 입력을 취소하고 돌아갑니다.")
                        continue
                        
                    try:
                        new_check = Checklist(title=title)
                        checklists.append(new_check)
                        print("✅ 체크리스트에 추가되었습니다!")
                    except ValueError as e:
                        print(f"❌ 오류: {e}")

                elif sub_choice == "2":
                    print("\n--- 👀 체크리스트 확인 ---")
                    if not checklists:
                        print("등록된 체크리스트가 없습니다.")
                    else:
                        sorted_checklists = sorted(checklists, key=lambda x: not x.is_completed)
                        for index, item in enumerate(sorted_checklists, 1):        #enumerate함수를 통해 리스트의 요소뿐만 아니라 번호까지 함께 가져왔습니다.여기서 1을 넣은 이유는 리스트는 0부터 시작하지만,보여줄 떄는 1번부터 시작하도록 하기 위함입니다.
                            print(f"{index}. {item.get_summary()}")

                elif sub_choice == "3":
                    print("\n--- ✔️ 체크리스트 완료 처리 (뒤로 가려면 'q' 입력) ---")
                    if not checklists:
                        print("완료 처리할 체크리스트가 없습니다.")
                        continue
                    
                    for index, item in enumerate(checklists, 1):
                        print(f"{index}. {item.get_summary()}")
                    
                    user_input = input("완료할 항목의 번호를 입력하세요: ").strip()
                    if user_input.lower() == 'q':
                        print("↩️ 작업을 취소하고 돌아갑니다.")
                        continue
                        
                    try:
                        num = int(user_input)
                        if 1 <= num <= len(checklists):
                            checklists[num - 1].mark_as_completed()
                            print(f"✅ '{checklists[num - 1].title}' 항목이 완료 처리되었습니다!")
                        else:
                            print("❌ 올바른 번호 범위가 아닙니다.")
                    except ValueError:
                        print("❌ 숫자 또는 'q'만 입력해 주세요.")
                else:
                    print("❌ 잘못된 선택입니다. 다시 입력해주세요.")

        elif main_choice == "q":
            print("\n👋 프로그램을 종료합니다. 좋은 하루 되세요!")
            break
        else:
            print("❌ 올바른 메뉴 번호를 입력해 주세요.")

if __name__ == "__main__":
    main()

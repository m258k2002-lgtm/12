def display_menu():
    print("\n" + "="*30)
    print(" 🎓 학생 성적 관리 프로그램")
    print("="*30)
    print(" 1. 학생 성적 입력")
    print(" 2. 전체 성적 조회")
    print(" 3. 프로그램 종료")
    print("="*30)

def main():
    # 학생들의 성적을 저장할 딕셔너리
    students_db = {}

    while True:
        display_menu()
        choice = input("원하는 메뉴의 번호를 선택하세요: ")

        if choice == '1':
            print("\n[성적 입력]")
            name = input("학생 이름을 입력하세요: ")
            
            try:
                kor = float(input("국어 점수를 입력하세요: "))
                eng = float(input("영어 점수를 입력하세요: "))
                math = float(input("수학 점수를 입력하세요: "))
                
                # 총점 및 평균 계산
                total = kor + eng + math
                avg = total / 3
                
                # 딕셔너리에 데이터 저장
                students_db[name] = {
                    '국어': kor,
                    '영어': eng,
                    '수학': math,
                    '총점': total,
                    '평균': avg
                }
                print(f"✅ {name} 학생의 성적이 성공적으로 저장되었습니다.")
                
            except ValueError:
                print("❌ [오류] 점수는 반드시 숫자로 입력해주세요!")

        elif choice == '2':
            print("\n[전체 성적 조회]")
            if not students_db:
                print("입력된 학생 데이터가 없습니다.")
            else:
                for name, data in students_db.items():
                    print(f"이름: {name} | 국어: {data['국어']} | 영어: {data['영어']} | "
                          f"수학: {data['수학']} | 총점: {data['총점']} | 평균: {data['평균']:.2f}")

        elif choice == '3':
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다! 👋")
            break

        else:
            print("❌ [오류] 잘못된 입력입니다. 1, 2, 3 중에서 선택해주세요.")

if __name__ == "__main__":
    main()
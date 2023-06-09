import parking_spot_manager
import file_manager
def start_process(path):
    """
        파일 경로를 받아와 파일을 읽어 이를 문자열 리스트 형태로 반환받은 후,
        해당 문자열 리스트를 parking_spot 인스턴스의 리스트로 변환하여 spots 변수에 할당한다.
    """
    str_list = file_manager.read_file(path)
    spots = parking_spot_manager.str_list_to_class_list(str_list)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            """
                사용자가 1을 입력할 경우
                parking_spot 인스턴스의 리스트를 매개변수로 하여, 해당 리스트의 요소 수,
                각 요소들의 정보를 출력한다.
                이후 다시 사용자 입력을 기다린다.
            """
            parking_spot_manager.print_spots(spots)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            """
                사용자가 4를 입력할 경우
                "Exit"를 출력한 후 반복문을 종료하여 더 이상 input을 받지 않는다.
            """
            print("Exit")
            break
        else:
            print("invalid input")
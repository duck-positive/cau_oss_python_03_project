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
            """
            사용자가 2를 입력할 경우
            필터 선택 목록을 출력한 후, 다시 사용자 입력을 기다린다.
            """
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                """
                    사용자가 1번을 입력한 경우
                    이름을 입력받아 parking_spot 객체의 리스트인 spots에서 name을 키로 하는 값이 사용자의 입력을 포함하는 객체들로 리스트를 만들어 반환받는다.
                    이를 임시 변수 filtered_spots에 할당한 후, 기존 객체 리스트를 삭제한 후, 임시 변수에 할당했던 리스트를 spots 변수에 할당한다.
                """
                keyword = input('type name:')
                filtered_spots = parking_spot_manager.filter_by_name(spots, keyword)
                del spots
                spots = filtered_spots
            elif select == 2:
                """
                    사용자가 2번을 입력한 경우
                    시도를 입력받아 parking_spot 객체의 리스트인 spots에서 city를 키로 하는 값이 사용자의 입력을 포함하는 객체들로 리스트를 만들어 반환받는다.
                    이를 임시 변수 filtered_spots에 할당한 후, 기존 객체 리스트를 삭제한 후, 임시 변수에 할당했던 리스트를 spots 변수에 할당한다.
                """
                keyword = input('type city:')
                filtered_spots = parking_spot_manager.filter_by_city(spots, keyword)
                del spots
                spots = filtered_spots
            elif select == 3:
                """
                    사용자가 3번을 입력한 경우
                    시군구를 입력받아 parking_spot 객체의 리스트인 spots에서 district를 키로 하는 값이 사용자의 입력을 포함하는 객체들로 리스트를 만들어 반환받는다.
                    이를 임시 변수 filtered_spots에 할당한 후, 기존 객체 리스트를 삭제한 후, 임시 변수에 할당했던 리스트를 spots 변수에 할당한다.
                """
                keyword = input('type district:')
                filtered_spots = parking_spot_manager.filter_by_district(spots, keyword)
                del spots
                spots = filtered_spots
            elif select == 4:
                """
                    사용자가 4번을 입력한 경우
                    주차장유형을 입력받아 parking_spot 객체의 리스트인 spots에서 ptype을 키로 하는 값이 사용자의 입력을 포함하는 객체들로 리스트를 만들어 반환받는다.
                    이를 임시 변수 filtered_spots에 할당한 후, 기존 객체 리스트를 삭제한 후, 임시 변수에 할당했던 리스트를 spots 변수에 할당한다.
                """
                keyword = input('type ptype:')
                filtered_spots = parking_spot_manager.filter_by_ptype(spots, keyword)
                del spots
                spots = filtered_spots
            elif select == 5:
                """
                    사용자가 5번을 입력한 경우
                    최소 위도, 최대 위도, 최소 경도, 최대 위도를 순서대로 입력받아 이를 locations라는 이름의 tuple로 만든 후 
                    parking_spot 객체의 리스트인 spots에서 latitude를 키로 하는 값이 최소 위도보다 크고 최대 위도보다 작으며, longitude를 키로 하는 값이 최소 경도보다 크고 최대 경도보다 작은 값들을 가진 객체들로 리스트를 만들어 반환받는다.
                    이를 임시 변수 filtered_spots에 할당한 후, 기존 객체 리스트를 삭제한 후, 임시 변수에 할당했던 리스트를 spots 변수에 할당한다.
                """
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locations = (min_lat, max_lat, min_lon, max_lon)
                filtered_spots = parking_spot_manager.filter_by_location(spots, locations)
                del spots
                spots = filtered_spots
            else:
                """
                    그 외의 사용자 입력에 대해서는 "invalid input"을 출력한다.
                """
                print("invalid input")
        elif select == 3:
            """
                사용자가 3을 입력할 경우
                정렬 기준으로 할 수 있는 키워드의 목록을 출력한 후, 다시 사용자 입력을 기다린다.
            """
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            """
                사용자 입력을 받아 만약 keywords에 없다면 'invalid input'을 출력하며,
                있다면 해당 keyword와 parking_spot_manager 객체 리스트 spots를 인수로 정렬 함수를 호출한 후, 정렬된 객체 리스트를 반환받는다.
                정렬된 객체 리스트는 임시 변수에 할당한 후, 기존 spots 리스트를 삭제 후, 임시 변수에 할당했던 정렬된 리스트를 spots에 할당한다.
            """
            if keyword in keywords:
                sorted_spot = parking_spot_manager.sort_by_keyword(spots, keyword)
                del spots
                spots = sorted_spot
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
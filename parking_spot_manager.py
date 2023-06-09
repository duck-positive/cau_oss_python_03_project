class parking_spot:
    """
        생성자
        자원명, 시도, 시군구, 주차장유형, 경도, 위도를 매개변수로 받아
        이를 __item 필드에 딕셔너리 형태로 저장한다.
        이때 경도와 위도는 실수로 변환하여 저장한다.
        Args :
            name (String) : 자원명
            city (String) : 시도
            district (String) : 시군구
            ptype (String) : 주차장유형
            longitude (String) : 경도
            latitude (String) : 위도
    """
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {"name" : name, "city" : city, "district" : district, 
                        "ptype" : ptype, "longitude" : float(longitude), "latitude" : float(latitude)}

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    """
        get 메서드 
        keyword를 매개변수로 받아 __item 필드에서 keyword를 키로 하는 값을 반환한다
        기본값은 'name'으로 설정한다.
        Args : 
            keyword (String) : __item 필드에서 접근하려는 값의 키. 기본값은 'name'
        Return : 
            (String) : __item 필드에서 keyword를 키로 하는 값
    """
    def get(self, keyword= 'name'):
        return self.__item[keyword]

"""
    문자열을 객체로 변환하는 함수
    문자열을 매개변수로 받아 각 요소마다 ','를 기준으로 분리하여 이를 매개변수로 parking_spot 인스턴스를 생성한다.
    Args:
        str_list (List<String>) : 무료주차장에 대한 정보의 List
    Return:
        (List<parking_spot>) : 매개변수의 각 요소를 parking_spot 인스턴스로 변환. 해당 인스턴스들을 담고 있는 List 
"""
def str_list_to_class_list(str_list):
    spots = []
    for row in str_list:
        row = row.split(',')
        one_spot = parking_spot(row[1], row[2], row[3], row[4], row[5], row[6])
        spots.append(one_spot)
    return spots
"""
    매개변수로 받은 spots 리스트의 요소들을 출력하는 함수
    spots의 총 요소 개수를 출력한 후, 각 요소들의 세부 정보를 출력한다.
    Args:
        spots (List<parking_spot>) : parking_spot의 리스트
"""
def print_spots(spots):
    print("---print elements({})---".format(len(spots)))
    for spot in spots:
        print(spot.__str__())

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
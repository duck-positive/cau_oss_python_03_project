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
"""
    이름을 기준으로 필터링하는 함수
    매개변수로 받은 spots 리스트에서 'name'을 키로 하는 값이 매개변수 name을 포함하는 객체들로만 리스트를 만들어 이를 반환한다.
    Args:
        spots (List<parking_spot>) : 필터링 하기 전의 객체 리스트
        name (String) : 필터링의 기준
    Return:
        (List<parking_spot>) : name을 기준으로 필터링 된 객체 리스트
    참고 : 리스트 함축(https://likethefirst.tistory.com/entry/Python-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%95%A8%EC%B6%95-List-Comprehension#:~:text=%5BPython%5D%20%EB%A6%AC%EC%8A%A4%ED%8A%B8%20%ED%95%A8%EC%B6%95%20%28List%20Comprehension%29%201%201.%20%ED%95%9C,%EC%9D%B4%EB%A3%A8%EB%8A%94%206%20-%203.%20%EC%84%A4%EB%AA%85%207%20%EC%B6%94%EA%B0%80%EB%90%98%EC%96%B4%20%EC%B6%9C%EB%A0%A5%EB%90%9C%EB%8B%A4)
"""
def filter_by_name(spots, name):
    filtered_list_by_name = [spot for spot in spots if spot.get().find(name) != -1]
    return filtered_list_by_name
"""
    시도를 기준으로 필터링하는 함수
    매개변수로 받은 spots 리스트에서 'city'를 키로 하는 값이 매개변수 city를 포함하는 객체들로만 리스트를 만들어 이를 반환한다.
    Args:
        spots (List<parking_spot>) : 필터링 하기 전의 객체 리스트
        city (String) : 필터링의 기준
    Return:
        (List<parking_spot>) : city를 기준으로 필터링 된 객체 리스트
    참고 : 리스트 함축(https://likethefirst.tistory.com/entry/Python-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%95%A8%EC%B6%95-List-Comprehension#:~:text=%5BPython%5D%20%EB%A6%AC%EC%8A%A4%ED%8A%B8%20%ED%95%A8%EC%B6%95%20%28List%20Comprehension%29%201%201.%20%ED%95%9C,%EC%9D%B4%EB%A3%A8%EB%8A%94%206%20-%203.%20%EC%84%A4%EB%AA%85%207%20%EC%B6%94%EA%B0%80%EB%90%98%EC%96%B4%20%EC%B6%9C%EB%A0%A5%EB%90%9C%EB%8B%A4)
"""
def filter_by_city(spots, city):
    filtered_list_by_city = [spot for spot in spots if spot.get('city').find(city) != -1]
    return filtered_list_by_city
"""
    시군구를 기준으로 필터링하는 함수
    매개변수로 받은 spots 리스트에서 'district'를 키로 하는 값이 매개변수 district를 포함하는 객체들로만 리스트를 만들어 이를 반환한다.
    Args:
        spots (List<parking_spot>) : 필터링 하기 전의 객체 리스트
        district (String) : 필터링의 기준
    Return:
        (List<parking_spot>) : district를 기준으로 필터링 된 객체 리스트
    참고 : 리스트 함축(https://likethefirst.tistory.com/entry/Python-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%95%A8%EC%B6%95-List-Comprehension#:~:text=%5BPython%5D%20%EB%A6%AC%EC%8A%A4%ED%8A%B8%20%ED%95%A8%EC%B6%95%20%28List%20Comprehension%29%201%201.%20%ED%95%9C,%EC%9D%B4%EB%A3%A8%EB%8A%94%206%20-%203.%20%EC%84%A4%EB%AA%85%207%20%EC%B6%94%EA%B0%80%EB%90%98%EC%96%B4%20%EC%B6%9C%EB%A0%A5%EB%90%9C%EB%8B%A4)
"""
def filter_by_district(spots, district):
    filtered_list_by_district = [spot for spot in spots if spot.get('district').find(district) != -1]
    return filtered_list_by_district
"""
    주차장유형을 기준으로 필터링하는 함수
    매개변수로 받은 spots 리스트에서 'ptype'을 키로 하는 값이 매개변수 ptype을 포함하는 객체들로만 리스트를 만들어 이를 반환한다.
    Args:
        spots (List<parking_spot>) : 필터링 하기 전의 객체 리스트
        ptype (String) : 필터링의 기준
    Return:
        (List<parking_spot>) : ptype을 기준으로 필터링 된 객체 리스트
    참고 : 리스트 함축(https://likethefirst.tistory.com/entry/Python-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%95%A8%EC%B6%95-List-Comprehension#:~:text=%5BPython%5D%20%EB%A6%AC%EC%8A%A4%ED%8A%B8%20%ED%95%A8%EC%B6%95%20%28List%20Comprehension%29%201%201.%20%ED%95%9C,%EC%9D%B4%EB%A3%A8%EB%8A%94%206%20-%203.%20%EC%84%A4%EB%AA%85%207%20%EC%B6%94%EA%B0%80%EB%90%98%EC%96%B4%20%EC%B6%9C%EB%A0%A5%EB%90%9C%EB%8B%A4)
"""
def filter_by_ptype(spots, ptype):
    filtered_list_by_ptype = [spot for spot in spots if spot.get('ptype').find(ptype) != -1]
    return filtered_list_by_ptype
"""
    위치를 기준으로 필터링하는 함수
    매개변수로 받은 spots 리스트에서 'latitude'를 키로 하는 값이 매개변수 locations의 0번째 값(최소 위도)보다 크고, 1번째 값(최대 위도)보다 작으며,
    'longitude'를 키로 하는 값이 2번째 값(최소 경도)보다 크고, 3번째 값(최대 경도)보다 객체들로만 리스트를 만들어 이를 반환한다.
    Args:
        spots (List<parking_spot>) : 필터링 하기 전의 객체 리스트
        locations (tuple<float>) : 필터링의 기준(최소 위도, 최대 위도, 최소 경도, 최대 경도 순)
    Return:
        (List<parking_spot>) : locations를 기준으로 필터링 된 객체 리스트
    참고 : 리스트 함축(https://likethefirst.tistory.com/entry/Python-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%95%A8%EC%B6%95-List-Comprehension#:~:text=%5BPython%5D%20%EB%A6%AC%EC%8A%A4%ED%8A%B8%20%ED%95%A8%EC%B6%95%20%28List%20Comprehension%29%201%201.%20%ED%95%9C,%EC%9D%B4%EB%A3%A8%EB%8A%94%206%20-%203.%20%EC%84%A4%EB%AA%85%207%20%EC%B6%94%EA%B0%80%EB%90%98%EC%96%B4%20%EC%B6%9C%EB%A0%A5%EB%90%9C%EB%8B%A4)
"""
def filter_by_location(spots, locations):
    filtered_list_by_locations = [spot for spot in spots if spot.get('latitude') > locations[0] and spot.get('latitude') < locations[1] and spot.get('longitude') > locations[2] and spot.get('longitude') < locations[3]]
    return filtered_list_by_locations
"""
    키워드를 기준으로 정렬하는 함수
    parking_spot 클래스의 객체 리스트 spots에서 keyword로 받은 인수를 키로 하는 값을 기준으로 정렬하는 함수
    Args:
        spots (List<parking_spot>) : 정렬하기 전의 객체 리스트
        keyword (String) : 정렬 기준
    Return:
        (List<parking_spot>) : keyword를 키로하는 값을 기준으로 정렬된 객체 리스트
"""
def sort_by_keyword(spots, keyword):
    sorted_list_by_keyword = sorted(spots, key= lambda key : key.get(keyword))
    return sorted_list_by_keyword
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
import re

## 기본이 되는 extract string을 넣고 빼는 형태로 만듬 기본이기 때문에 사용하고 있긴 하지만 모양만 사용할뿐 이 함수는 사용하지 않음##
def extract_and_modify_string(input_string):
    uncensored_present = 'Reducing Mosaic' in input_string
    suffix = '-u' if uncensored_present else ''
    
    pattern = r'([a-zA-Z]+-[0-9]+)(\.\w+)?'
    matches = re.findall(pattern, input_string)
    
    file_extension_match = re.search(r'\.\w+$', input_string)
    file_extension = file_extension_match.group(0) if file_extension_match else ''
    
    modified_matches = [match[0] + suffix + file_extension + (match[1] if match[1] else '') for match in matches]
    
    result_string = ' '.join(modified_matches)
    
    return result_string

## extract extract_fc2ppvnumber, extract_fileextension, extract_reducingmosic, extract_modelnumber을 전부 통합한 함수##
def extract_perpect(input_string):
    # 변수 모음 장소 (예외 처리) 
    # S : 시작
    uncensored_present  = 'Reducing Mosaic' in input_string
    FC2PPV_present      = 'FC2PPV'          in input_string
    # e : 끝
    
    # 변수 모음 장소
    # S : 시작
    suffix = ''         # uncensored
    matches = ''        # 파일 이름 
    file_extension = '' # 확장자
    # e : 끝
    
    # suffix를 지정하는 구간 (Reducing Mosic) 
    # S : 시작
    if uncensored_present:
        suffix  =       extract_reducingmosic(uncensored_present)   # suffix를 extract하는 함수 (Reducing Mosic)
    # e : 끝
    
    # matches를 지정하는 구간 
    # S : 시작
    if FC2PPV_present: 
        matches =       extract_fc2ppvnumber(input_string)          # matches를 extract하는 함수 (fc2일 경우)
    else:       
        matches =       extract_modelnumber(input_string)           # matches를 extract하는 함수 (fc2가 아닐 경우)
    # e : 끝
    
    
    # file_extension를 지정하는 구간 (확장자)
    file_extension =    extract_fileextension(input_string)         # 확장자를 extract하는 함수
    
    # match + suffix + file_extension 를 완성 시키는 구간
    modified_matches = [match[0] + suffix + file_extension + (match[1] if match[1] else '') for match in matches]
    
    # return하는 string로 이루어진 배열이라면 하나의 string으로 변경을 해주었다.
    result_string = ' '.join(modified_matches)
    
    return result_string

## 특정 내용을 찾는 함수 1번 ##
def extract_reducingmosic(input_string):
    suffix = '-u' if input_string else ''
    
    return suffix

## 특정 내용을 찾는 함수 2번 ##
def extract_modelnumber(input_string):
    pattern = r'([a-zA-Z]+-[0-9]+)(\.\w+)?'
    
    matches = re.findall(pattern, input_string)
    
    return matches

## 특정 내용을 찾는 함수 3번 ##
def extract_fc2ppvnumber(input_string):
    pattern = r'FC2PPV\s+(\d+)'
    
    match = re.search(pattern, input_string)
    if match:
        number = match.group(1)
    else:
        number = "No match found"
    
    return [("FC2-PPV-" + number, '')]

## 특정 내용을 찾는 함수 4번 ##
def extract_fileextension(input_string):
    file_extension_match = re.search(r'\.\w+$', input_string)
    
    file_extension = file_extension_match.group(0) if file_extension_match else ''
    
    return file_extension
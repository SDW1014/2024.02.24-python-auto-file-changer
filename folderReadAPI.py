import os
import re

#directory_path를 기준으로 그 안에 있는 파일들의 정보를 전부 가져온다. 
def list_files_in_directory(directory_path):
    entries = os.listdir(directory_path)
    
    files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
    
    return files

# 지금 py가 들어있는 경로를 가져온다. 
def find_now_directory():
    return os.getcwd()

# file_path라는 경로에 있는 파일의 title을 new_title로 변경한다.
def set_file_title(file_path, new_title):
    directory = os.path.dirname(file_path)
    
    
    new_file_path = os.path.join(directory, new_title) if directory else new_title # ? : 의 삼항 연산자에 익숙한데 ifelse도 익숙해져야겠지 그렇다고 한다 이게 python의 삼항이다. 
    
    os.rename(file_path, new_file_path)
    
    return new_file_path

# [".mp4", ".ts"]를 체크를 하고있음
def extract_fileextension_checker(input_string):
    matching_extensions = [".mp4", ".ts"]
    file_extension_match = re.search(r'\.\w+$', input_string)
    
    if file_extension_match:
        extracted_extension = file_extension_match.group()  # 확장자 추출
        if extracted_extension in matching_extensions:
            return True
    return False

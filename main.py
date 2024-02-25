import folderReadAPI, titleChanger

def main():
    first_main_function_file_read_and_title_change()
    
if __name__ == "__main__":
    main()
    
## main의 첫번째 함수
### 1. 파일을 읽는다. 
### 2. 파일을 읽어서 나온 file_list(리스트)를 반복 한다. 
### 3. 파일의 리스트들 중 extract_fileextension_checker()를 이용해서 mp4...등 유형들을 판단한다. 
### 4. 맞는 유형에 따라 set_file_title()으로 이름을 변경해준다. 
def first_main_function_file_read_and_title_change():
    file_list = folderReadAPI.list_files_in_directory(folderReadAPI.find_now_directory())
    for file in file_list:
        if folderReadAPI.extract_fileextension_checker(file):
            folderReadAPI.set_file_title(file, titleChanger.extract_perpect(file))
import folderReadAPI, titleChanger

def main():
    file_list = folderReadAPI.list_files_in_directory(folderReadAPI.find_now_directory())
    for file in file_list:
        if folderReadAPI.extract_fileextension_checker(file):
            folderReadAPI.set_file_title(file, titleChanger.extract_perpect(file))
    
if __name__ == "__main__":
    main()
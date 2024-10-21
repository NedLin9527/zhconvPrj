import os
import zhconv

def convert_filenames_to_traditional_chinese(directory):
    # 取得指定目錄下所有 mp4 檔案
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            # 將檔案名稱的簡體中文轉為繁體中文
            traditional_name = zhconv.convert(filename, 'zh-tw')
            # 獲取舊檔案的完整路徑
            old_file_path = os.path.join(directory, filename)
            # 獲取新檔案的完整路徑
            new_file_path = os.path.join(directory, traditional_name)
            # 重命名檔案
            os.rename(old_file_path, new_file_path)
            print(f"已將 {filename} 轉換為 {traditional_name}")

# 指定目錄路徑
directory_path = "/your/directory/path"
convert_filenames_to_traditional_chinese(directory_path)

from pathlib import Path
import os

list_of_files = [
    
    "app.py",
    "reseach/test.py",
    "reseach/test.ipynb",
    ".env",
    "requirements.txt"
    
]

for files in list_of_files:
    files_path = Path(files)
    
    dir_name,file_name = os.path.split(files_path)
    print(dir_name,file_name)
    
    if dir_name:
        os.makedirs(dir_name,exist_ok=True)
    if not os.path.exists(files_path):
        with open(files_path,'w') as f:
            pass
    else:
        print("not file existsS")
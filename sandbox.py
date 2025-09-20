import os
os.scandir(".")
for entry in os.scandir("."):
    print(entry)
    print(entry.stat())
    print(entry.path, "Directory" if entry.is_dir() else "File")
import files_db

db = files_db.create("C:\\")
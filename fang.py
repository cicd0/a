from zipfile import ZipFile 
file_name = "fang.zip"
with ZipFile(file_name, "r") as zip:
    zip.extractall(path="fang", pwd="mischief".encode("utf-8"))

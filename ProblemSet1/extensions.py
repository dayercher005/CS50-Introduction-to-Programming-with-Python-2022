fileName = input("Enter the file name")

fileName = fileName.strip()

if fileName[-5:].lower() == ".jpeg":
    print("image/jpeg")
else:
    match fileName[-4:].lower():
        case ".gif":
            print("image/gif")
        case ".jpg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

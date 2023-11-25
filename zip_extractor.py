import zipfile


def extract_archive(zip_path, direcotry):
    with zipfile.ZipFile(zip_path, "r") as archive:
        archive.extractall(r"{direcotry}")


if __name__ == '__main__':
    extract_archive(r"C:\Users\ahmed\OneDrive\Pictures\Screenshots\New folder\asd.zip",
                    r"C:\Users\ahmed\OneDrive\Pictures\Screenshots\New folder")

    print("Extraction complete")

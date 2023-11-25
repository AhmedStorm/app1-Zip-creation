import zipfile
import pathlib


def make_archieve(file_paths, dir):
    name = f"{pathlib.Path(dir).name}.zip"
    output = pathlib.Path(dir, name)
    with zipfile.ZipFile(output, "w") as archieve:
        for path in file_paths:
            path = pathlib.Path(path)
            archieve.write(path, arcname=path.name)


if __name__ == "__main__":
    make_archieve([r"Not_Part_of_Project\Spiderman.py",
                  r"Not_Part_of_Project\asd.py"], "Not_Part_of_Project")

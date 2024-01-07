import zipfile
import pathlib


def make_archive(files, tgt_path):
    dir = pathlib.Path(tgt_path, "compressed.zip")
    with zipfile.ZipFile(dir, 'w') as archive:

        for file in files:
            filepath = pathlib.Path(file)
            archive.write(filepath, arcname=filepath.name)


def extract_archive(archive_file, tgt_path):
    with zipfile.ZipFile(archive_file, "r") as archive:
        archive.extractall(tgt_path)


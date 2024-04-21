import os
import glob
import shutil

from natsort import natsorted


def group_and_move(source_directory: str, destination_directories) -> None:
    _create_destination_directories(destination_directories)

    files = list(filter(os.path.isfile, glob.glob(source_directory + "/*.txt")))

    files.sort(key=lambda x: os.path.getmtime(x))
    _move_by_odd_even_group(files, destination_directories)


def _create_destination_directories(destination_directories):
    for directory in destination_directories:
        if not os.path.exists(directory):
            os.makedirs(directory)


def _move_by_odd_even_group(files, destination_directories):
    for i in range(len(files)):
        _move(files[i], destination_directories[i % 2])


def _move(file: str, destination_directory: str) -> None:
    file_name = file.split("/")[-1]
    print(f"Moving {file} to {destination_directory}")
    shutil.move(file, f"{destination_directory}/{file_name}")


if __name__ == "__main__":
    source_directory = "examples"
    destination_directories = ["questions", "answers"]
    group_and_move(source_directory, destination_directories)

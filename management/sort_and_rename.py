import glob
import os


def main(source_directory: str) -> None:
    files = list(filter(os.path.isfile, glob.glob(source_directory + "/*.txt")))
    files.sort(key=lambda x: os.path.getmtime(x))

    for index, file in enumerate(files):
        file_name, file_extension = os.path.splitext(file)
        old_file_name = f"{file_name}{file_extension}"
        new_file_name = f"{index + 1}{file_extension}"
        print(f"Replacing {old_file_name} to {new_file_name}")
        os.rename(f"{old_file_name}", f"{source_directory}/{new_file_name}")


if __name__ == "__main__":
    main("examples")

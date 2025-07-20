import os
from datetime import datetime, timedelta

creations = [
    {"folder_name": "yyyy-mm-ddhhMM", "folder_path": "fakemorefolders"},
]

files_per_folder = 10
date_range = "3 month"
file_content_prefix = "this is mock content"

supported_formats = [
    {"name_format": "yyyy-mm-ddhhMM", "python_date_format": "%Y-%m-%d%H%M"}
]


def main() -> None:
    for creation in creations:
        if "month" in date_range:
            days = _months_to_days(date_range)
        end_date = datetime.today()
        start_date = end_date - timedelta(days=days)

        folder_path = creation["folder_path"]
        folder_name = creation["folder_name"]

        # Make sure folder exists
        os.makedirs(folder_path, exist_ok=True)

        current_date = start_date
        while current_date <= end_date:
            new_folder_name = folder_name
            file_content = None
            for supported_format in supported_formats:
                if supported_format["name_format"] in folder_name:
                    replace_str = current_date.strftime(
                        supported_format["python_date_format"]
                    )

                new_folder_name = new_folder_name.replace(
                    supported_format["name_format"], replace_str
                )
                file_content = f"{file_content_prefix} - {replace_str}"

            if new_folder_name == folder_name:
                print("Unsupported folder name format")
                exit

            new_folder_path = os.path.join(folder_path, new_folder_name)
            os.makedirs(new_folder_path, exist_ok=True)

            print(f"Created folder: {new_folder_path}")

            for i in range(1, files_per_folder + 1):
                new_file_name = f"{i}.txt"
                file_path = os.path.join(new_folder_path, new_file_name)

                with open(file_path, "w") as f:
                    f.write(file_content)

            current_date += timedelta(days=1)


def _months_to_days(months_str):
    num = int(months_str.split()[0])
    return num * 30


if __name__ == "__main__":
    main()

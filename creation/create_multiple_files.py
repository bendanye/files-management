import os
import calendar
import uuid
from datetime import datetime, timedelta

creations = [
    {"file_name": "helloWorld_yyyymmdd.csv", "folder_path": "fakecsvfolders"},
    {"file_name": "iamtesting_dd-MMM-yyyy.log", "folder_path": "fakelogfolders"},
    {"file_name": "iamtesting_dd-MMM-yyyy-HHMM.log", "folder_path": "fakelogfolders"},
    {"file_name": "epoch-iamtesting-uuid.log", "folder_path": "fakejsonfolders"},
]

date_range = "3 month"
file_content_prefix = "this is mock content"

SUPPORTED_FORMATS = [
    {"file_format": "yyyymmdd", "python_date_format": "%Y%m%d"},
    {"file_format": "dd-MMM-yyyy-HHMM", "python_date_format": "%d-%b-%Y-%H%M"},
    {"file_format": "dd-MMM-yyyy", "python_date_format": "%d-%b-%Y"},
    {"file_format": "epoch"},
    {"file_format": "uuid"},
]


def main() -> None:
    for creation in creations:
        if "month" in date_range:
            days = _months_to_days(date_range)
        end_date = datetime.today()
        start_date = end_date - timedelta(days=days)

        folder_path = creation["folder_path"]
        file_name = creation["file_name"]

        # Make sure folder exists
        os.makedirs(folder_path, exist_ok=True)

        current_date = start_date
        while current_date <= end_date:
            new_file_name = file_name
            file_content = None
            for supported_format in SUPPORTED_FORMATS:
                if supported_format["file_format"] in file_name:
                    if supported_format["file_format"] == "epoch":
                        replace_str = str(calendar.timegm(current_date.timetuple()))
                    elif supported_format["file_format"] == "uuid":
                        replace_str = str(uuid.uuid4())
                    else:
                        replace_str = current_date.strftime(
                            supported_format["python_date_format"]
                        )

                    new_file_name = new_file_name.replace(
                        supported_format["file_format"], replace_str
                    )
                    file_content = f"{file_content_prefix} - {replace_str}"

            if new_file_name == file_name:
                print("Unsupported file name format")
                exit

            file_path = os.path.join(folder_path, new_file_name)

            with open(file_path, "w") as f:
                f.write(file_content)

            print(f"Created file: {file_path}")

            current_date += timedelta(days=1)


def _months_to_days(months_str: str) -> int:
    num = int(months_str.split()[0])
    return num * 30


if __name__ == "__main__":
    main()


def get_file_name(path: str) -> str:
    """Extract the file name (including extension) from the path."""
    path = path.replace("\\", "/")  # Normalize backslashes to forward slashes
    return path.split("/")[-1]

def get_file_name_without_extension(path: str) -> str:
    """Extract the file name (without extension) from the path."""
    file_name = get_file_name(path)
    return file_name.split(".")[0] if "." in file_name else file_name

file_path = input("Enter the file path: ").strip()

# Normalize the file path
file_path = file_path.replace("\\", "/")  # Replace backslashes with forward slashes

print("File name with extension:", get_file_name(file_path))
print("File name without extension:", get_file_name_without_extension(file_path))
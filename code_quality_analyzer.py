import os

def analyze_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    total_lines = len(lines)
    blank_lines = sum(1 for line in lines if not line.strip())
    comment_lines = sum(1 for line in lines if line.strip().startswith("#"))

    print("Code Quality Report")
    print("-------------------")
    print(f"Total Lines: {total_lines}")
    print(f"Blank Lines: {blank_lines}")
    print(f"Comment Lines: {comment_lines}")

if __name__ == "__main__":
    file_name = input("Enter Python file name: ")
    
    if os.path.exists(file_name):
        analyze_file(file_name)
    else:
        print("File not found.")

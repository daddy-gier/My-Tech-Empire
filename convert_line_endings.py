import os

def convert_crlf_to_lf(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        
        content = content.replace(b'\r\n', b'\n')
        
        with open(file_path, 'wb') as f:
            f.write(content)
        
        print(f"Converted {file_path} to LF")
    except Exception as e:
        print(f"Error converting {file_path}: {e}")

def find_md_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        # Exclude .git directory
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file.endswith(".md"):
                yield os.path.join(root, file)

if __name__ == "__main__":
    for md_file in find_md_files("."):
        convert_crlf_to_lf(md_file)

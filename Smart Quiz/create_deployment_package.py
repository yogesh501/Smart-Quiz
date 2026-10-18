"""
Helper script to package Smart Quiz into a clean zip file
ready for GitHub / Render deployment.
Excludes large local binaries (like cloudflared.exe), cache files, etc.
"""

import os
import zipfile

EXCLUDE_DIRS = {'.git', '.vscode', '__pycache__', '.idea', 'venv', 'env', '.venv'}
EXCLUDE_FILES = {'cloudflared.exe', 'smart_quiz_deploy.zip'}
EXCLUDE_EXTENSIONS = {'.pyc', '.pyo'}

def create_package(output_zip="smart_quiz_deploy.zip"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, output_zip)
    
    count = 0
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            # Prune excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            
            for file in files:
                if file in EXCLUDE_FILES:
                    continue
                if any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                    continue
                
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                zipf.write(full_path, rel_path)
                count += 1
                
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"[PACKAGE] Successfully created '{output_zip}' ({count} files, {file_size_kb:.1f} KB).")
    return output_path

if __name__ == "__main__":
    create_package()

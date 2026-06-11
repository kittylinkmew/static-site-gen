import os
import shutil


def copy_files_recursive(source_dir, dest_dir):
    os.mkdir(dest_dir)
    dir_list = os.listdir(source_dir)
    for item in dir_list:
        dest_path = os.path.join(dest_dir, item)
        source_path = os.path.join(source_dir, item)
        if os.path.isfile(source_path):
            print(f"Copying {source_path} to {dest_path}")
            shutil.copy(source_path, dest_path)
        else:
            copy_files_recursive(source_path, dest_path)

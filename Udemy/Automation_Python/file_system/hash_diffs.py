import zipfile
import os
# --- ZIPPING FILES AND FOLDERS ---

def zip_single_file(source_file_path, target_archive_path):
    print('Creating archive: {}'.format(target_archive_path))
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
        print('Compression will be used')
    except:
        compression = zipfile.ZIP_STORED
        print('No compression will be used')
    with zipfile.ZipFile(target_archive_path, mode='w') as zf:
        print('Adding file: {}'.format(source_file_path))
        zf.write(source_file_path,
                 arcname = os.path.basename(source_file_path),
                 compress_type=compression)
    print('Done')


def zip_folder_recursively(source_folder_path, target_archive_path):
    print('Zipping folder: {}'.format(source_folder_path))
    print('Creating archive: {}'.format(target_archive_path))
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
        print('Compression will be used')
    except:
        compression = zipfile.ZIP_STORED
        print('No compression will be used')
    with zipfile.ZipFile(target_archive_path, mode='w') as zf:

        #walk the folder tree
        print("before")
        print(source_folder_path)
        for folder, subfolders, files in os.walk(source_folder_path):

            for f in files:
                print(source_folder_path)
                path = os.path.join(source_folder_path, folder, f)
                print('Adding file: {}'.format(path))
                zf.write(
                    path,
                    arcname = os.path.relpath(os.path.join(folder, f),
                                              source_folder_path),
                    compress_type=compression)
    print('Done\n')



if __name__ == '__main__':
    import pathlib

    src_file = (pathlib.Path('.') / 'myfile.txt').resolve()
    scr_folder = (pathlib.Path('.') / 'Udemy').resolve()
    target_zippedfile = os.path.join('.', 'myzippedfile.zip')
    target_zippedfolder = os.path.join('.', 'myzippedfolder.zip')

    # zip a single file
    #zip_single_file(str(src_file), target_zippedfile)

    # zip a folder recursively
    zip_folder_recursively(str(scr_folder),target_zippedfolder)







import sys
import shutil
import os
import multiprocessing
import time
def mkdir_ifnot_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

wav_path = sys.argv[1]
save_root = sys.argv[2]
max_cpu = int(sys.argv[3])

def cp_wav(filename, i, dirpath):
    if filename.endswith('.wav') or filename.endswith('.WAV'):

        filename_path = os.sep.join([dirpath, filename])
        save_dir_name = dirpath.split('/')[-1]
        if i == 0:
            save_path = os.sep.join([save_root, 'verify', save_dir_name])
        else:
            save_path = os.sep.join([save_root, 'enroll', save_dir_name])
        mkdir_ifnot_exist(save_path)
        print(filename_path, '∑(っ°Д°;)っ ☆ミ ☆ミ', save_path)
        shutil.copy(filename_path, save_path)




if __name__ == '__main__':
    start = time.time()
    pool = multiprocessing.Pool(processes = max_cpu)
    for (dirpath, dirname, filename_list) in os.walk(wav_path):
        if len(filename_list) == 1:
            continue
        for i, filename in enumerate(filename_list):
            pool.apply_async(cp_wav, (filename, i, dirpath))
            #pool.apply(cp_wav, (filename, i, dirpath))
    pool.close()
    pool.join()
    end = time.time()
    print('time is : ', end - start)





from time import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line != '':
            all_data.append(line.strip('\n'))
            line = file.readline()


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

# start_time = time()
# for file in files:
#     read_info(file)
# end_time = time()
# print(f'Время выполнения задачи линейно: {round((end_time - start_time), 2)} c')

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        start_time = time()
        result = pool.map(read_info, files)
        end_time = time()
        print(f'Время выполнения задачи многопроцессорно: {round((end_time - start_time), 2)} c')

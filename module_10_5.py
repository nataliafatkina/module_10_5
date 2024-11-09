from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line != '':
            all_data.append(line.strip('\n'))
            line = file.readline()


files = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.now()
# for file in files:
#     read_info(file)
# end = datetime.now()
# print(end - start)

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        start = datetime.now()
        result = pool.map(read_info, files)
        end = datetime.now()
        print(end - start)

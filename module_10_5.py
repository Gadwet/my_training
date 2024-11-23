import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Код для проверки:
start = datetime.datetime.now()
for f in filenames:
    read_info(f)
end = datetime.datetime.now()
print(f'Время работы линейного вызова: {end - start}')

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'Время работы многопроцессорного вызова: {end - start}')
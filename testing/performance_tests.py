import time
import sorting

def test_sorting_performance():
    data = [5, 3, 8, 4, 2]
    start_time = time.time()
    sorted_data = sorting.sort(data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Sorting took {elapsed_time} seconds")

if __name__ == '__main__':
    test_sorting_performance()

import numpy as np
import input5a
# use a generator


def gen_maze(num_array):
    curr_ind = 0
    curr_arr = num_array
    steps = 0

    def cycle():
        nonlocal curr_ind
        nonlocal curr_arr
        nonlocal steps
        while 1:
            new_ind = curr_ind + curr_arr[curr_ind]
            curr_arr[curr_ind] += 1
            curr_ind = new_ind
            steps += 1
            try:
                if curr_arr[curr_ind]:
                    yield "keep going"
            except: 
                yield steps
    return cycle


def main():
    sample_array = input5a.input
    for check in gen_maze(sample_array)():
        if check != "keep going":
            print("Steps it takes:")
            print(check)
            break

if __name__ == "__main__":
    main()

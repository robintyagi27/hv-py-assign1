import multiprocessing

def stress():
    while True:
        pass

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    print(f"Stressing {cores} CPU cores...")

    processes = []
    for _ in range(cores):
        p = multiprocessing.Process(target=stress)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

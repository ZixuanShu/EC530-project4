import multiprocessing
import time

#set maximium processer number as 2, since my computer have a 12 cores cpu.
PROCESSES = multiprocessing.cpu_count() - 10

def stubs(secs):
    time.sleep(secs)
    return 0

def stub_queue():
    print(f"Running with {PROCESSES} processes!")

    start = time.time()
    with multiprocessing.Pool(PROCESSES) as p:
        p.map_async(
            stubs,
            [
                10,
                8,
                2,
                6,
                5,
            ],
        )
        # clean up
        p.close()
        p.join()

    print(f"Time taken = {time.time() - start:.10f}")

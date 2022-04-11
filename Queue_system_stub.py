import multiprocessing
import time

#set maximium processer number as 6, since my computer have a 12 cores cpu.
PROCESSES = multiprocessing.cpu_count()/2

def stubs(secs):
    time.sleep(secs)
    return 0

def stub_queue(input_array):
    print(f"Running with {PROCESSES} processes!")

    start = time.time()
    with multiprocessing.Pool(PROCESSES) as p:
        p.map_async(
            stubs,
            input_array,
        )
        # clean up
        p.close()
        p.join()
    time_used = time.time() - start
    print(f"Time taken = {time_used:.10f}")
    return time_used 


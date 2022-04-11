import multiprocessing
import time
import speech_recognition as sr

#set maximium processer number as 6, since my computer have a 12 cores cpu.
PROCESSES = multiprocessing.cpu_count()/2

def transcribe(Filename):
    r = sr.Recognizer()
    harvard = sr.AudioFile(Filename)
    with harvard as source:
        audio = r.record(source)
    string = r.recognize_google(audio)
    return string

def transcribe_queue(input_arr):
    print(f"Running with {PROCESSES} processes!")

    start = time.time()
    results = []
    with multiprocessing.Pool(PROCESSES) as p:
        results = p.map_async(
            transcribe,
            input_arr,
        ).get()
        # clean up
        p.close()
        p.join()

    print(f"Time taken = {time.time() - start:.10f}")
    return results


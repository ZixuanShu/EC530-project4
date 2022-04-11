import multiprocessing
import time
import speech_recognition as sr

#set maximium processer number as 2, since my computer have a 12 cores cpu.
PROCESSES = multiprocessing.cpu_count() - 10

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

if __name__ == '__main__': 

    output = transcribe_queue([
    'test_audios/Sample1.wav',
    'test_audios/Sample2.wav',
    'test_audios/Sample3.wav',
    'test_audios/Sample4.wav',
    'test_audios/Sample5.wav',
    'test_audios/Sample6.wav',
    ])

    print(output)


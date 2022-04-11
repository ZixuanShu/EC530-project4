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
    print(string)
    return string

def transcribe_queue():
    print(f"Running with {PROCESSES} processes!")

    start = time.time()
    with multiprocessing.Pool(PROCESSES) as p:
        p.map_async(
            transcribe,
            [
                'Sample1.wav',
                'Sample2.wav',
                'Sample3.wav',
                'Sample4.wav',
                'Sample5.wav',
                'Sample6.wav',
            ],
        )
        # clean up
        p.close()
        p.join()

    print(f"Time taken = {time.time() - start:.10f}")

transcribe('Sample1.wav')
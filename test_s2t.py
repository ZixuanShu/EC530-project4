import Queue_system_speech

expected_output = 'generating random paragraphs can be excellent way for writers to get their creative flow going at the beginning of the day'

def test_transcribe():
    resulting_output = Queue_system_speech.transcribe('test_audios/Sample1.wav')
    assert resulting_output == expected_output
import Queue_system_speech

expected_output = ['generating random paragraphs can be excellent way for writers to get their creative flow going at the beginning of the day', 'the writer has no idea what topic the random paragraph of Abby about by that pierce', 'this forces the right her to use creativity to come complete valve Street Hammond writing challenges to write a short story and a beautiful Ahmad', "a second option is to use to random paragraph somewhere in a short story they create the third option is to have to run them paragraph pizza and you're probably not true story no matter which of these challenges is undertaken the writer is forced to to use creativity to incorporate a paragraph into their writing", "a random paragraph can also be an actual invite for a writer to tackle writer's block", "completely random paragraph on ways to begin take down some of the issues that may have been causing the writer's block in the first place"]

test_input = [
'test_audios/Sample1.wav',
'test_audios/Sample2.wav',
'test_audios/Sample3.wav',
'test_audios/Sample4.wav',
'test_audios/Sample5.wav',
'test_audios/Sample6.wav',
]

def test_speech_queue():
    resulting_output = Queue_system_speech.transcribe_queue(test_input)
    for (word1, word2) in zip(expected_output, resulting_output):
        assert word1 == word2
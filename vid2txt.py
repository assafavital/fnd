import moviepy.editor as MP
import speech_recognition as SR
from pydub import AudioSegment
import argparse
import os

class AudioExtractor:

    def __init__(self):
        pass

    def extract(self, file):
        vid = MP.VideoFileClip("{}.mp4".format(file))
        output_file = "{}.wav".format(audio_path)
        vid.audio.write_audiofile(output_file)
        # AudioSegment.from_mp3(output_file).export("{}.wav".format(audio_path), format="wav")


class TextExtractor:

    def __init__(self):
        pass

    def extract(self, audio_path, text_path):
        recognizer = SR.Recognizer()
        with SR.AudioFile("{}.wav".format(audio_path)) as source:
            audio = recognizer.record(source)

        recognized = recognizer.recognize_sphinx(audio)
        print(recognized)

        with open(text_path, "w") as f:
            f.write(recognized)


### MAIN
ap = argparse.ArgumentParser()
ap.add_argument("file", type=str)
args = ap.parse_args()

extractor = AudioExtractor()
extractor.extract(args.file)

TextExtractor().extract(args.output, "{}.txt".format(args.file))
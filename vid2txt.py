import moviepy.editor as MP
import speech_recognition as SR
from pydub import AudioSegment
import argparse
import os

class AudioExtractor:

    def __init__(self):
        pass

    def extract(self, video_path, audio_path):
        vid = MP.VideoFileClip(video_path)
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

        print(recognizer.recognize_sphinx(audio))


### MAIN
ap = argparse.ArgumentParser()
ap.add_argument("input", type=str)
ap.add_argument("output", type=str)
args = ap.parse_args()

extractor = AudioExtractor()
extractor.extract(args.input, args.output)

TextExtractor().extract(args.output, "nofile")
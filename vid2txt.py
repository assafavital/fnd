import moviepy.editor as MP
import speech_recognition as SR
from pydub import AudioSegment
import argparse, os

class FNDVid2Txt:

    def __call__(self, filename):
        """
        Execute audio transcription from video file.
        :param filename: Video file name (only mp4 files are supported)
        :return:
        """
        self.vidFile = "{}.mp4".format(filename)
        self.wavFile = "{}.wav".format(filename)
        self.txtFile = "{}.txt".format(filename)
        self.extract_audio()
        self.extract_text()
        print("Transcription is available at {}".format(self.txtFile))

    def extract_audio(self):
        print("Extracting audio from {} ...".format(self.vidFile))
        vid = MP.VideoFileClip(self.vidFile)
        vid.audio.write_audiofile(self.wavFile)

    def extract_text(self):
        print("Transcribing speech from {} ...".format(self.wavFile))
        recognizer = SR.Recognizer()
        with SR.AudioFile(self.wavFile) as audioSource:
            text = recognizer.recognize_sphinx(recognizer.record(audioSource))
            with open(self.txtFile, "w") as txtOutput:
                txtOutput.write(text)

if __name__ == "__main__":
    # Argument Parsing
    argparser = argparse.ArgumentParser()
    argparser.add_argument("file", type=str)
    args = argparser.parse_args()

    # Text Extraction
    vid2txt = FNDVid2Txt()
    vid2txt(args.file)

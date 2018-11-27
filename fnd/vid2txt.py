import moviepy.editor as MP
import speech_recognition as SR
from pydub import AudioSegment
import argparse, os
from fnd.logger import log

class FNDVid2Txt:

    def __call__(self, filename, therealdeal=False):
        """
        Execute audio transcription from video file.
        :param filename: Video file name (only mp4 files are supported)
        :return:
        """
        self.vidFile = "{}.mp4".format(filename)
        self.wavFile = "{}.wav".format(filename)
        self.txtFile = "{}.txt".format(filename)
        self.therealdeal = therealdeal
        self.extract_audio()
        self.extract_text()
        log("Transcription is available at {}".format(self.txtFile))
        # print("Transcription is available at {}".format(self.txtFile))
        if self.therealdeal:
            return open(self.txtFile, "r").read()
        return ""

    def extract_audio(self):
        log("Extracting audio from {} ...".format(self.vidFile))
        # print("Extracting audio from {} ...".format(self.vidFile))
        vid = MP.VideoFileClip(self.vidFile)
        vid.audio.write_audiofile(self.wavFile)

    def extract_text(self, therealdeal=False):
        log("Transcribing speech from {} ...".format(self.wavFile))
        # print("Transcribing speech from {} ...".format(self.wavFile))
        recognizer = SR.Recognizer()
        if self.therealdeal:
            with SR.AudioFile(self.wavFile) as audioSource:
                # credentials = open("creds.json", "r").read()
                text = recognizer.recognize_sphinx(recognizer.record(audioSource))#, credentials_json=credentials)#"17633f0219a85a1c7a730d98bbf790c1445320c4")
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

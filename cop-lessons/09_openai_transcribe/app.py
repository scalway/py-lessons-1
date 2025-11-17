import os

from openai import OpenAI

client = OpenAI()

def trascribeFile(f:str):
    audio_file = open(f, "rb")
    transcription = client.audio.transcriptions.create(
        model = "gpt-4o-transcribe",
        file = audio_file,
        response_format = "text"
    )

    return transcription

def transcribeFileToStrFile(inFile:str):
    res = trascribeFile(inFile)
    # safe res to file
    with open(f"transcription.txt", "a") as f:
        f.write(f"\n >>> FILE: {inFile}\n")
        f.write(res)

    return res


def main():
    folder = "/home/slovic/Projekty/study/py-lessons-1/py-lessons-1/audio/lecture_6"
    files = sorted(os.listdir(folder))
    for file in files:
        print("starting file:", file)
        res = transcribeFileToStrFile(os.path.join(folder, file))
        print(res)

if __name__ == "__main__":
    main()
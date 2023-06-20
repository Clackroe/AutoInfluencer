import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, ImageClip
from moviepy.video.tools.subtitles import SubtitlesClip


def editDaMovie(outputDir, clipDir, inputDir):

    gmplyClip = VideoFileClip(
        f"{clipDir}/" + random.choice(os.listdir(clipDir)))

    clipLength = int(gmplyClip.duration)

    audio = AudioFileClip(f"{inputDir}/speech.mp3")
    audioLength = int(audio.duration)

    image = ImageClip(f"{inputDir}/screenshot.png").to_ImageClip().set_start(
        0).set_duration(2).set_position(("center", "center"))

    os.system(f"autosub {inputDir}/speech.mp3")

    def generator(txt): return TextClip(txt, font="Cooper Black", fontsize=95, color="white", bg_color="transparent",
                                        method="caption", align="center", size=(gmplyClip.w, gmplyClip.h)).set_position(("center", 0.75))
    subs = SubtitlesClip(f"{inputDir}/speech.srt", generator)

    subs = SubtitlesClip(subs, generator)

    endPoint = random.randint(audioLength+5, clipLength-5)

    bgClip = gmplyClip.subclip(int(endPoint - audioLength), endPoint)

    bgClip = bgClip.set_audio(audio)

    CompositeVideoClip([bgClip, image, subs]).write_videofile(
        f"{outputDir}/final.mp4", threads=4, fps=24)

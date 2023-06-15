import os, random

from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip

def editMovie(path):
    
    clip = VideoFileClip('gameplay-clips/' + random.choice(os.listdir('gameplay-clips')))
    
    
    clipLength = int(clip.duration)
    
    audio = AudioFileClip(path + 'speech.mp3')
    
    audioLength = int(audio.duration)
    
    os.system(f'autosub {path}/speech.mp3')
    
    
    generator = lambda txt: TextClip(txt, font='Bernard-MT-Condensed', fontsize=40,  color='white', stroke_color='black', stroke_width=1.5, bg_color='transparent', method='caption', align='center', size=(clip.w, clip.h))
    subs = SubtitlesClip(path + 'speech.srt', generator)
    
    subtitles = SubtitlesClip(subs, generator)
    
    
    
   
    
    
    
    
    endPoint = random.randint(audioLength+5, clipLength-5)
    
    backgroundClip = clip.subclip(int(endPoint - audioLength), endPoint)
    
    mainClip = backgroundClip.set_audio(audio)
    
    mainClip = CompositeVideoClip([mainClip, subtitles.set_position(('center', 0.6))])
    
    mainClip.write_videofile(path + 'final.mp4')
    
    
    
    
    
    
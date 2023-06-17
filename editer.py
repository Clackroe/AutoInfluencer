import os, random

from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, ImageClip
# from moviepy.video.fx.resize import resize
from moviepy.video.tools.subtitles import SubtitlesClip

def editMovie(path):
    
    clip = VideoFileClip('gameplay-clips/' + random.choice(os.listdir('gameplay-clips')))
    
    
    clipLength = int(clip.duration)
    
   
    
    
    
    audio = AudioFileClip(path + 'speech.mp3')
    
    audioLength = int(audio.duration)
    
    image = ImageClip(f'{path}/post.png').to_ImageClip().margin(bottom=350).set_start(0).set_duration(audioLength).set_position(('center', 'bottom'))
    
    image = image.resize((image.w * 1.5, image.h * 1.5))
    
    os.system(f'autosub {path}/speech.mp3')
    
    
    generator = lambda txt: TextClip(txt, font='Cooper Black', fontsize=95,  color='white', bg_color='transparent', method='caption', align='center', size=(clip.w, clip.h)).set_position(('center', 0.75))
    subs = SubtitlesClip(path + 'speech.srt', generator)
    
    subtitles = SubtitlesClip(subs, generator)
    
        
    endPoint = random.randint(audioLength+5, clipLength-5)
    
    backgroundClip = clip.subclip(int(endPoint - audioLength), endPoint)
    
    mainClip = backgroundClip.set_audio(audio)
    
    mainClip = CompositeVideoClip([mainClip, image, subtitles], use_bgclip=True)
    
    #Currently not working 100%. The image crops out the video below it
    
    # mainClip.resize(width=1280, height=720)
    
    
    mainClip.write_videofile(path + 'final.mp4', threads=8, fps=24)
    
    
    
    
    
    
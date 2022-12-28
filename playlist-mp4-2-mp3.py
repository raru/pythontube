from moviepy.editor import AudioFileClip
from pytube import Playlist
import os

def Download(link):
  youtubeObject = Playlist(link)
  # youtubeObject = youtubeObject.streams.get_audio_only() 
  try:
    for video in youtubeObject.videos:
      # video.streams.filter(only_audio=True).first().download(output_path="/Users/raru/Public/Root/pythontube/pythontube/downloads") 
      filename = video.streams.get_audio_only().download(output_path="/Users/raru/Public/Root/pythontube/pythontube/downloads")
      clip = AudioFileClip(filename)
      clip.write_audiofile(filename[:-4]+".mp3")
      os.remove(filename)
      clip.close()
  except:
    print("Deu ruim em baixar!")
  print("Deu bom em baixar! Uhuuuuuu")

link = input("POE O LINK DA PLAYLIST AQUI XUXU: ")
Download(link)
from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  # youtubeObject = youtubeObject.streams.get_audio_only() 
  try:
    youtubeObject.download(output_path="/Users/raru/Public/Root/pythontube/pythontube/downloads")
  except:
    print("Deu ruim em baixar!")
  print("Deu bom em baixar! Uhuuuuuu")

link = input("put yout ytube link here!! URL: ")
Download(link)
from pytube import YouTube 
import os

yt=YouTube(input("Enter Youtube link:"))
yd= yt.streams.filter(only_audio=True).first()
destination="/Users/AbhishekGadhia/Desktop"

out_file=yd.download(output_path=destination)

base, ext= os.path.splitext(out_file)
new_file=base+".mp3"
os.rename(out_file, new_file)


print("Title:",yt.title)
print("Views:", yt.views)

print(yt.title+" has been successfully downloaded")


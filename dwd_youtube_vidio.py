#import pytube library to download the vidio
import pytube
#Ask for the url of vidio
url1=input("enter url:")
#we can take path as well
path=input("enter path of  storage:")
#here the line to download the vidio
pytube.YouTube(url1).streams.get_highest_resolution().download(path)
print("download successfully")


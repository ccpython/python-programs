#youtube purser 
#create a html 4.0 friendly embedcode from
#youtube url.

from Tkinter import *
import tkMessageBox
clip = Tk()
youtubeurl= clip.selection_get(selection = "CLIPBOARD")  #gets url from clipboard
if "youtube.com" in youtubeurl:
    clip.clipboard_clear()# clears current contents of clipboard
    videoloc=youtubeurl.find("v=")#finds the video id in youtube url
    videocode=youtubeurl[videoloc+2:]#extract the video id from the youtube url
    #below creates the embed html 4.0 friendly code
    embedcode = '<object width="420" height="315"><param name="movie" value="//www.youtube.com/v/'+videocode+'?autoplay=1&version=3&hl=en_US"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="//www.youtube.com/v/'+videocode+'?autoplay=1&version=3&hl=en_US" type="application/x-shockwave-flash" width="420" height="315" allowscriptaccess="always" allowfullscreen="true"></embed></object>'
    clip.clipboard_append(embedcode)#copys embeded code for user to paste where they wish
    tkMessageBox.showinfo("Done!","You can now paste this code\nanywhere html4 and shockwave-flash is allowed")
else:
    tkMessageBox.showwarning("Error:","Not a Valid youtube url")

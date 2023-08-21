import speedtest,tkinter as tk
from tkinter import font
# Get Local Serve To Testing The Speed
network = speedtest.Speedtest()
server = network.get_best_server()
# Define Tkinter
root = tk.Tk()
root.title("NetSpeed") # Program Title
root.resizable(False,False)
custom_font = font.Font(size=25)
speed_font = font.Font(size=17)
root.config(bg="#4181e8")
label = tk.Label(root,text="Network Speed Test",pady=25,fg="white",font=custom_font,bg="#4181e8")
label.pack()
speed = tk.Label(root,pady=25,fg="white",font=speed_font,bg="#4181e8") # Create the speed label once
speed.pack()
# Keep Refreshing
def update_speed():
    global network, speed # Use global variables
    download_speed = network.download() / 10 ** 6 # Mbps's
    upload_speed   = network.upload() / 10 ** 6 # Mbps's
    speed.config(text=f" Download Speed {download_speed:.2f} Mbps\nUpload Speed {upload_speed:.2f} Mbps") # Update the speed label text

update_speed() # Call the function for the first time
root.mainloop() # Load Gui

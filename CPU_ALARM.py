import psutil
import pyttsx3 #you have to" pip install pyttsx3 " in the terminal first

utilizare_cpu = psutil.cpu_percent(interval=1)
print(f"Utilizarea CPU: {utilizare_cpu}%")
engine = pyttsx3.init()
if utilizare_cpu > 8.0:
 engine.say(f"Your CPU usage is at {utilizare_cpu} precent")
 engine.runAndWait()
get_property_engine = engine.getProperty('rate') #Makes it so you can make it faster or slower
engine.setProperty('rate', get_property_engine + 100) #Changes the speed (you can make it faster or slower)
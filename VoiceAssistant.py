import schedule
import requests
import time
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
    
class ontime:
    
  def say(self):
    speak.Speak(self.script)
    
  def __init__(self, time, script):
    self.time = time
    self.script = script
    schedule.every().day.at(self.time).do(self.say)

class onminute:
    
  def say(self):
    speak.Speak(self.script)
    
  def __init__(self, time, script):
    self.time = time
    self.script = script
    schedule.every(self.time).minutes.do(self.say)

hki = get("https://api.steve.fi/Helsinki-Temperature/data/")

'''
Examples:
ontime("9:56", "Test 1")
ontime("10:56", "test 2")
ontime("17:30", "test 3")

onminute(1, "once a minute")
onminute(5, "every 5 minutes")

'''

ontime("6:00", "Good morning Master today "+time.strftime("%A")+" "+time.strftime("%x")+" current temperature is" + str(hki)+ "degree celcius")


while True:
    schedule.run_pending()
    time.sleep(1)
    


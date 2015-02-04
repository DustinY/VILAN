import speech
import win32com.client
import time

def response(phrase, listener):
	print "You said %s" % phrase
	if phrase.lower() == "turn off":
		listener.stoplistening()
	elif phrase.lower() == "open chrome" or phrase.lower() == "open browser":
		shell = win32com.client.Dispatch("WScript.Shell")
		shell.Run("chrome")
	elif phrase.lower() == "add a bookmark" or phrase.lower() == "add a book mark":
		shell = win32com.client.Dispatch("WScript.Shell")
		shell.SendKeys("^d", 0)
	elif phrase.lower() == "open e-mail" or phrase.lower == "open the mail":
		shell = win32com.client.Dispatch("WScript.Shell")
		shell.SendKeys("^l", 0)
		time.sleep(1);
		shell.SendKeys("gmail.com~", 0)
	elif phrase.lower() == "go back" or phrase.lower() == "go backward":
		shell = win32com.client.Dispatch("WScript.Shell")
		shell.SendKeys("%{LEFT}", 0)
	elif phrase.lower() == "go forward" or phrase.lower() == "go front":
		shell = win32com.client.Dispatch("WScript.Shell")
		shell.SendKeys("%{RIGHT}", 0)
	elif phrase.lower() == "close browser" or phrase.lower() == "close chrome":
		shell = win32com.client.Dispatch("WScript.Shell")
		shell.SendKeys("%{F4}", 0)

listener = speech.listenforanything(response)

# Your program can do whatever it wants now, and when a spoken phrase is heard,
# response() will be called on a separate thread.
while listener.islistening():
	time.sleep(1)
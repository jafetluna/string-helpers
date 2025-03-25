import pyperclip
from plyer import notification

def getCount():
    clipboard_text = pyperclip.paste()
    notification.notify(
    title='',
    message=f'{len(clipboard_text)} caracteres',)

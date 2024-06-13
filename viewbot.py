from pyfiglet import Figlet
import webbrowser
import time
from colorama import Fore, Back, Style
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,  
                    webbrowser.BackgroundBrowser(chrome_path)) 
f = Figlet(font='slant')
print(Fore.RED + f.renderText('VIEWBOT'))
print(Fore.BLUE + 'made by saksham')
a = (input("enter youtube url: "))
for i in range(100):
    webbrowser.get('chrome').open_new_tab(a)
   
    

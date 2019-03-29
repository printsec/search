import pyautogui
import pyfiglet
from selenium import webdriver
from termcolor import colored
import time
import sys

def asciiBanner():
    banner = pyfiglet.figlet_format("Search")
    return banner

print(colored(asciiBanner(), 'blue'))
print(colored("creator: printsec", 'red'))
print("\n\n")

Search = input("What do you wanna search for?: ")

browser = webdriver.Chrome()
sida = ("https://google.com/?#q;")
browser.get(sida)
time.sleep(1)
pyautogui.typewrite(Search)
pyautogui.press("enter")
print("Here you go!")
sys.exit()

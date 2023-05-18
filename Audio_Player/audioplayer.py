import numpy as np
import random
from playsound import playsound
import os
from tkinter import *
from tkinter import Tk
import tkinter as tk
from pygame import mixer
import pygame
import time
audio=[]
def Play(audio):
    while(1):
        a=np.random.randint(1,21)
        v="Songs/Song"+str(a)+".mp3"
        if(len(audio)==20):
            break
        if v in audio:
            continue
        else :
            audio.append(v)
    return audio
    
class MusicPlayer:
    def __init__(self, window):
        self.audio=audio
        self.window = window
        self.window.title("Music Player")
        window.geometry('750x300')
        # create the UI elements
        self.label = tk.Label(window, text="Audio Player")
        self.label.pack()
        
        self.button = tk.Button(window, text="Play", command=self.play_music)
        self.button.pack(pady=5)
        
        self.button = tk.Button(window, text="Next", command=self.next_music)
        self.button.pack(pady=5)
        
        self.button = tk.Button(window, text="Pause", command=self.pause_music)
        self.button.pack(pady=5)
        
        self.button = tk.Button(window, text="Resume", command=self.unpause_music)
        self.button.pack(pady=5)
                
        pygame.mixer.init()
        self.musicPlaying = False
    
    def check_end(self):
        if not pygame.mixer.music.get_busy() and self.musicPlaying:
            self.next_music()
        else:
            self.window.after(100,self.check_end)
            
    def play_music(self):
        # self.audio=Play(audio)
        if(len(audio)==0):
            self.audio=Play(audio)
        a=self.audio.pop()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()
        Lower_left = tk.Label(root,text =a)
        Lower_left.place(relx = 0.0,
                 rely = 1.0,
                 anchor = 'sw')
        print(a)
        self.musicPlaying = True
        self.window.after(100,self.check_end)
        
    def next_music(self):
        pygame.mixer.music.stop()
        if(len(audio)==0):
            self.audio=Play(audio)
        a=self.audio.pop()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()
        Lower_left = tk.Label(root,text =a)
        Lower_left.place(relx = 0.0,
                 rely = 1.0,
                 anchor ='sw')
        print(a)
        self.musicPlaying = True
    
    def pause_music(self):
        self.musicPlaying = False
        if not self.musicPlaying:
            pygame.mixer.music.pause()
            
            
    def unpause_music(self):
        if not self.musicPlaying:
            pygame.mixer.music.unpause()
            self.musicPlaying = True
        
root = tk.Tk()
player = MusicPlayer(root)
root.mainloop()
            
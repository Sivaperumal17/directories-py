#!/usr/bin/python 
import requests



def request (url):
        try:
              return  requests.get("http://"+url)
        except requests.expections.connectionError:
               pass

target_url=input("[*]enter target url:")
file_name=input("[*] Enter file to use:")
file=open(file_name,"r")
for line in file:
         word=line.strip()
         full_url=word+"."+ target_url
         response=request(full_url)
         if response:
                 print("[+]Discovered subdomine at this link:"+full_url)

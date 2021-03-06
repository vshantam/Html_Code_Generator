#usr/bin/bash/Python3
"""UTF-8 encoding"""
import sys
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    choice='y'
    try:
        while(choice=='y'):
            url=""#Post your url here {or}
            url=input("Please enter the url for the web page that need to be parsed:\n")#input url for website
            if(url[:8]!='https://'):
                print("Sorry!!!\n Not a propper url \nPlease try again\n")#checking for propper url format
            else:
                get_url=urlopen(url)#getting response from server
                get_code=get_url.read()#extracting html code
                soup=BeautifulSoup(get_code,'lxml')#parsing
                soup=soup.find('html').encode('utf-8')#taking care for encoding error
                print("The HTML code :\n\n\n")
                print(soup)#Displaying the entire HTML code
                soup=BeautifulSoup(get_code,'lxml')
                link_count=len(soup.find_all("a"))#counting the number of hyertext link
                print("The Hyper link present in the page are {}".format(link_count))
                for i in range(len(soup.find_all("a"))):
                    print("For {}::The url is ::{}".format(soup.find_all("a")[i].text.encode('utf-8'),soup.find_all("a")[i].get('href').encode('utf-8')))#Displaying the hyper text links with their links
                choice=input("Do you Wish to continue?(Yes/No)".strip())
                choice=choice.lower()[0]
    except KeyboardInterrupt:
            print ("{}" .format('Exiting Script\nInterrupted by the user\n'))#Taking care of Exceptions
    
    except Exception as e:
        print("An Error occured\nPlease try again later\n")
        print("Error code:{}".format(str(e)))

if __name__=='__main__':
    main()


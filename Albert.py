#/usr/bin/env python3 
# -*- coding: utf-8 -*-
try:
    import urllib
    from urllib.request import urlopen
    import http.client
    from urllib import parse
    import shodan
    import sys
    import nmap
    import optparse
    from api import apikey
    from tqdm import tqdm as tqdm
    import time
    import os
    import platform
    import time
except (ImportError) as e:
    print("Something is terribly wrong:\n->{}".format(e))

api = shodan.Shodan(apikey)    
def albert_faces():
    alberts = ''
    albert = random.randint(1, 3)
    if albert == 1:alberts = "./albert_face.txt"
    if albert == 2:alberts = "./albert_face_2.txt"
    if albert == 3: alberts = "./fat_albert_3"
    face = open(alberts, "r")
    lulz = face.readlines()
    for line in lulz:
        print(line.strip("\n")
        time.sleep(0.5)
    print("Loading The King Himself Hopefully He Left You Some Exploits....")
    print("Gr33ts: Chef Gordon, Root, Johnny 5")

test = platform.system()
if test == 'Windows': clear = 'cls'
elif test == 'Linux': clear = 'clear'
elif test == 'Java': clear = 'clear'
elif test == '':
    print("[ ! ] Exiting, you have an unknown system! [ ! ] ")
    sys.exit(1)
def progress_bar(duration):
    for i in tqdm(range(int(duration))):
        time.sleep(1)

def write_file(line):
    with open('hosts_list', 'at') as f:
        f.writelines(line)
    f.close()
    return False

def list_reject(target = ''):
    try:
        search = api.host(target)
        # id_seen = set()
        print("""
                IP: {}
                Organization: {}
                Operating System: {}
        """.format(search['ip_str'], search.get('org', 'n/a'), search.get('os', 'n/a')))

        # Print all banners
        for item in search['data']:
            print("""
                        Port: {}
                        Banner: {}
                """.format(item['port'], item['data']))
            oops = [str(search['ip_str'], "\n", str(search['data'], "\n"))]
            write_file(''.join(oops))
        return False
    except shodan.APIError as e:
        os.system(clear)
        logo = '''
         ________   __        _______   ______   ______   _________   
        /_______/\ /_/\     /_______/\ /_____/\ /_____/\ /________/\  
        \::: _  \ \\:\ \    \::: _  \ \\::::_\/_\:::_ \ \\__.::.__\/  
         \::(_)  \ \\:\ \    \::(_)  \/_\:\/___/\\:(_) ) )_ \::\ \    
          \:: __  \ \\:\ \____\::  _  \ \\::___\/_\: __ `\ \ \::\ \   
           \:.\ \  \ \\:\/___/\\::(_)  \ \\:\____/\\ \ `\ \ \ \::\ \  
            \__\/\__\/ \_____\/ \_______\/ \_____\/ \_\/ \_\/  \__\/ 
        is Restarting'''
        print('[✘] Errpr: %s' % e)
        option = input('[*] Shieeeet you wanna chagne that API Key? <Y/n>: ').lower()
        if option.startswith('y'):
            os.system(clear)
            file = open('api.py', 'w')
            SHODAN_API_KEY = input('[*] Hey! Hey! Hey! Enter A Valid Shodan.io API Key: ')
            oppsie = ["apikey= ", "\"",  str(SHODAN_API_KEY), "\""]
            file.write(''.join(oppsie))
            print('[~] File Dropped Nigga: ./api.py')
            file.close()
            print('[~] Take 5 To Larp Around\n {}'.format(logo))
            return False

def nmapScan(tgtHost, tgtPort):  # Nmap function created
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print("[ ! ]  {}\n TCP: {} \n UP/DOWN: {}\n".format(tgtHost, tgtPort, state))
    return False

if __name__ == '__main__':
    run = 't'
    albert_faces()
    test_system()
    while run == 't':
        try:
            os.system(clear)
            options = str(input("[ + ] Would you like to use:\n"
                       "1.) Shodan\n"
                       "2.) Nmap(Targeted Scanning of host system written out to XML file)\n"
                       "->"))
            if options == '1':
                os.system(clear)
                choice = str(input("[ + ] Is this a file list, or a single IP:\n"
                           "1.) File List\n"
                           "2.) Single IP\n"
                           "->"))
                if choice == '1':
                    os.system(clear)
                    dest = str(input("[ + ] Please input the name of the file list:\n->"))
                    liz = set()
                    if dest == '':
                        os.system(clear)
                        print("[ ! ] Hey! Hey! Hey! Need a file name! [ ! ]")
                        run = 'a'
                    reader = open(dest, "r")
                    for line in reader.readlines():
                        line.strip("\n")
                        list_reject(line)
                if choice == '2':
                    os.system(clear)
                    choice = str(input("[ + ] Please Input the IP: \n->"))
                    list_reject(choice)

            if options == '2':
                os.system(clear)
                host = str(input("[ + ] Please input host IP:\n->"))
                port = str(input("[ + ] Please input port:\n->"))
                nmapScan(host, port)
            if options == '':
                os.system(clear)
                print("[ ! ] Please enter a value! [ ! ]")
                print("[ ?? ] Exiting! [ ?? ]")
                sys.exit(1)
        except:
            raise

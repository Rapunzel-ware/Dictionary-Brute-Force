import time, zipfile
from colorama import Fore
import os
from colored import fg, bg, attr


print('''
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

--~~BioXsec Bruteforce Tool~~ ->	https://github.com/BioXsec
''')



print('[ Initializing program ]')



zipName = input("[+] Enter Zip File Path : ") or './usr/share/wordlists/rockyou.txt'
pwdsFile = input("[+] Enter Wordlist Path : ")





print('''[+] Brute Force Initiating ...''')
time.sleep(3)
print('''[+] Checking For Correct Password ...''')


if os.path.exists(zipName):
    if os.path.exists(pwdsFile):
        with open(pwdsFile,'rb') as text:
            for entry in text.readlines():
                password = entry.strip()
                with zipfile.ZipFile(zipName,'r') as zf:
                    try:
                        zf.extractall(pwd=password)

                        print("[+] Password Found!\n" + attr("reset"))

                        data = zf.namelist()[0]
                        print("Data: " + str(data))

                        data_size = zf.getinfo(data).file_size
                        print("Data Size: " + str(data_size))

                        print("Password: " + password.decode("utf-8"))

                        break
                    except:
                        print("[-] Password Not Found! - " + password.decode("utf-8"))
                    pass
    else:
        print("[-] Password File Not Found!")
else:
    print("[-] Zip File Not Found!")


input()


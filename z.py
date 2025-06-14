import telebot
import os
import time
import random
import threading

# Bot Token
token = "7535476931:AAHCMFyHGY7ymWXcqauUekqlmNJh_SJDnA0"
bot = telebot.TeleBot(token)

APPROVED_USERS_FILE = "approved_users.txt"
approved_users = []
admins = [7774742430]  # Replace with your Telegram ID
owner_id = 7774742430
stop_gali = False

def load_approved_users():
    users = []
    if os.path.exists(APPROVED_USERS_FILE):
        with open(APPROVED_USERS_FILE, "r") as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) == 2:
                    users.append({'id': int(data[0]), 'username': data[1]})
    return users

def save_approved_users():
    with open(APPROVED_USERS_FILE, "w") as f:
        for user in approved_users:
            f.write(f"{user['id']},{user['username']}\n")

approved_users = load_approved_users()

galis = [
    "Teri maa ki chut me solar panel laga dunga",
    "Teri maa ki gaand me RGB light laga dunga",
    "Teri maa ki chut me Bluetooth speaker daal ke gali FM chala dunga",
    "Tere baap ka lund flipkart me sale pe daal dunga",
    "Teri maa ki chut me WiFi router daal ke sabko internet de dunga",
    "Teri maa ki chut me notepad khol ke code likh dunga",
    "Teri maa ki aakh",
    "Bhosdike",
    "Madarchod",
    "Behenchod",
    "Randi ke bacche",
    "Kutte",
    "Chutiya",
    "Gandu",
    "Teri maa ka bhosda",
    "Baap se panga"
    "Tere baap ka naala 😆",
    "Teri behen ki chatri 🌂",
    "Teri gaand mein danda 🤣",
    "Teri maa ki chut me DJ bass 🔊",
    "Tere baap ki moochon me patakha 🎇",
    "Teri behen ki sari hawa me uda dunga 🎭",
    "Teri maa ka bhosda Gol Gappa banake kha jaunga 😜",
    "Teri gaand me torch dal ke light house bana dunga 🔦",
    "Teri maa ki chut me namak daal dunga 🌊",
    "MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA 🤣🤣", 
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA", 
    "TERI MAA K BHOSDE ME AEROPLANE PARK KARKE UDAAN BHAR DUGA ✈️🛫", 
    "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA 💣",
    "TERI MAAKI CHUT ME SCOOTER DAAL DUGA👅",  
    "TERE BHAI KI CHUT ME JHAADU LAGA DUNGA", 
    "Bhadhava Maderchod Bhosadike teri bhn ko chodu chutiya gandu scammer chut kay gulaam 😡😡🥵", 
    "Sunn Scammer Mai teri ma ko chodke apna lund chusakay aur tujhe apni jhaat chatake tujhe esa bhai dunga jo meri zindagi mai baar baar choosne ke liye taiyaar hojayenge 😂🥵🤢", 
    "teri maa ki chut me nimbu ka achar daalkr chode dalunga sale scammer kay fate hue condom ki aulad 😡🥵", 
    "jhaatu scammer teri jhant mein kerosene daal kar aag laga dunga Hijde ki kaali gaand 🥵🤢", 
    "Teri Gaand Mein Kutte Ka Lund kutiya ki paidayish scammer 😡🤮", 
    "Teri Jhaatein Kaat Kar Tere Mooh Par Laga Kar Unki scam French Beard Bana Doonga", 
    "Chullu Bhar Muth Mein Doob Mar bhaadu scammer Chut Ke Pasine Main apni kaak gand chuda bhosdike", 
    "kaali gand kay fatey hue lund jhaatu scammer kaas ush din Tera baap condom use kar leta betichod 🤬🤬", 
    "scammer hathi kay lund ka bhsoda bna kar teri kaali gand mai de dunga chhipakali ki choot jesi sakal kay 🤬🖕", 
    "Randi ki Najais lode tere jese chutiya scammer randi k baccho ko bachpan mai maar dena chiye", 
    "Chipkali ki bhigi chut Choot kay baal Chipkali ke jhaat ke paseene",
    "Gote Kitne Bhi Badey Ho, Lund Ke Niche Hi Rehtein Hain",
    "chutiye behenchod lauda madarchod gaandu bhosadikey",
    "Chullu Bhar Muth Mein Doob Mar Kaali Chut Ke Safed Jhaat",
    "chut kay baal nipple ki dhaar teri gaand mai Road roller de dunga 🖕🤬",
    "Teri Gaand Mein Kutte Ka Lund 🖕 Teri Jhaatein Kaat Kar Tere Mooh Par Laga Kar Unki French Beard Bana Doonga!",
    "Phatele Nirodh Ke Natije! 😂😂",
    "Teri maa ki choot gand kay tatto teri maa ka bhosda karke uski gaand mai ping pong kar dunga",
    "GAND KII DHAAR BHOSDIKE FATEE HUE CONDOM KI NAAJAIS PAIDAISH",
    "Teri ma ka bhosda sale maderchod ki aulad 🤬",
    "madarchod chutmarke teri tatti jesi shakl pe pad dunga bhen k lode chutiye",
    "maa k lode tere jese randi k baccho ko bachpan mai maar dena chiye",
    "TERA BAAP JOHNY SINS CIRCUS KAY BHOSDE JOKER KI CHIDAAS 14 LUND KI DHAAR TERI MUMMY KI CHUT MAI 200 INCH KA LUND",
    "teri ma Randi tera baap hizda kaali gaand kay Khade baal jhaatu Randi kay chodu",
    "SALA TARI BHAN KO ROAD PA LAJA KA KA NANGA KAR KA BAACHO SA CHUD VAU",
    "teri maa k bhosde mai MDH CHANA MASALA daal k tere baap ko vo spicy bhosda khila dunga 🥵🤮",
    "GAND MAI VIMAL KI GOLI BNA KAR DE DUNGA BHENCHO TERI GAAND MAI RAILWAY STATION KA FATAK DE DUNGA 😂😂🤬🖕",
    "14 baap ki Najais olad randi kay beez chinnale",
    "TARI MAA KI HARAAMJAALE BHOSDE PE MARUNGA LAATH TO TARI MIYAA CHUDEGI DINO RAAT",
    "Teri ma ki gand me hathi ka lund dalke asa chodunga Na Bacha hojayega Johny sins ,ke lund se chudwaungu bhosdike",
    "madar chod bhosdke esa lagta h apne hii taaate kaat ke chipka diya apni shakal dekh lodee jese shakal aur gand me h aakal",
    "teri ma ki choot randi kay scammer apne baap kay rupye se Jhaat kay baal trim kra lena 😂😂🤢",
    "bhsodike mujhe ye samajh nhi aata scam Karke kya tum jese loog apni mummy ka Randi naach dekhne jaate hoi 😂😂",
    "Jitno ka tunne scam kia na sbb teri maa k bhosde mai momos daal ke tere baap ko vo spicy bhosda khila Dengey 🥵🤮",
    "ek baar tu mill gya na tere scam kay paiso se teri gaand mai ungli de dunga or teri mummy se apna lund chusa kar chod dunga usko 🖕🥵🖕🥵🖕🤬😤🤢",
    "betichod le 100 rs. lele mujhse or apni mummy ki choot dikha de 😤😤 tujhe bhaut sock hai logo kay rupye scam karne ka 🥵🖕",
    "Randi kay scammer bhenchod 🤢 sale tum scammer loog har jagah apni maa kyo chudaane aa naate ho 🥵🤬",
    "scammer randi ki olad Jhatal teri maa ka bhosda sale mia Khalifa ki najais olad 🖕🖕",
    "Jhatal si sikal kay lund ki dhaar bhenchodd or kitne logo kay rupye scam karke apni gaand mai daalta hai 🤬😡",
    "teri bhn ko chodu 🥵 scam kay Paiso se apni mummy kay lie condom khareed lie jhaatu 😂",
    "🖕Scammer maderchod teri maa ka bhosda 🤮🤢 sale 2 koodi kay lund🤬🤬",
    "TARE DADA KE MUH PE MARUNGA LAATH TO TARI MIYAA CHUDEGI DONO RAAT",
    "BAHEN KE LAWDE AWAAZ UTA AWAAZ NHI AA RAHA TARI MAA KA BHOSDA",
    "TARI MAA KA BHOSDA",
    "TARI MAA KI CHUT",
    "Tere baap ka lund ke mooch se violin bajake gali compose kar dunga",
    "Tere baap ka lund ke mooch se violin bajake gali compose kar dunga aur livestream chalu kar dunga",
    "Tere baap ka lund ke mooch se violin bajake gali compose kar dunga aur sab galiyan sunenge",
    "Tere baap ka lund ke mooch se violin bajake gali compose kar dunga bina charger ke",
    "Tere baap ka lund ke mooch se violin bajake gali compose kar dunga bina permission ke",
    "Tere baap ka lund ke mooch se violin bajake gali compose kar dunga bina reboot ke",
    "Tere baap ka lund ke mooch se violin bajake gali compose kar dunga fir usko chaat jaunga",
    "Tere baap ka lund ko Flipkart pe sale pe daal dunga",
    "Tere baap ka lund ko Flipkart pe sale pe daal dunga aur livestream chalu kar dunga",
    "Tere baap ka lund ko Flipkart pe sale pe daal dunga aur usme ad laga dunga",
    "Tere baap ka lund ko Flipkart pe sale pe daal dunga bina charger ke",
    "Tere baap ka lund ko Flipkart pe sale pe daal dunga bina data loss ke",
    "Tere baap ka lund ko Flipkart pe sale pe daal dunga bina permission ke",
    "Tere baap ka lund ko Flipkart pe sale pe daal dunga jise sab report karenge",
    "Tere baap ka lund ko OnlyFans pe daal dunga",
    "Tere baap ka lund ko OnlyFans pe daal dunga aur livestream chalu kar dunga",
    "Tere baap ka lund ko OnlyFans pe daal dunga bina permission ke",
    "Tere baap ka lund ko OnlyFans pe daal dunga bina reboot ke",
    "Tere baap ka lund ko OnlyFans pe daal dunga fir usko chaat jaunga",
    "Tere baap ka lund ko OnlyFans pe daal dunga jise sab report karenge",
    "Tere baap ka lund me AirPods daal ke gaane chala dunga",
    "Tere baap ka lund me AirPods daal ke gaane chala dunga aur livestream chalu kar dunga",
    "Tere baap ka lund me AirPods daal ke gaane chala dunga aur sab galiyan sunenge",
    "Tere baap ka lund me AirPods daal ke gaane chala dunga aur usme ad laga dunga",
    "Tere baap ka lund me AirPods daal ke gaane chala dunga bina charger ke",
    "Tere baap ka lund me AirPods daal ke gaane chala dunga bina reboot ke",
    "Tere baap ka lund me AirPods daal ke gaane chala dunga fir usko chaat jaunga",
    "Tere baap ka lund me AirPods daal ke gaane chala dunga jise sab report karenge",
    "Tere baap ka lund me Bluetooth speaker daal ke gali FM chala dunga",
    "Tere baap ka lund me Bluetooth speaker daal ke gali FM chala dunga aur livestream chalu kar dunga",
    "Tere baap ka lund me Bluetooth speaker daal ke gali FM chala dunga bina charger ke",
    "Tere baap ka lund me Bluetooth speaker daal ke gali FM chala dunga bina data loss ke",
    "Tere baap ka lund me Bluetooth speaker daal ke gali FM chala dunga bina reboot ke",
    "Tere baap ka lund me Bluetooth speaker daal ke gali FM chala dunga jise sab report karenge",
    "Tere baap ka lund me DJ system daal dunga",
    "Tere baap ka lund me DJ system daal dunga aur livestream chalu kar dunga",
    "Tere baap ka lund me DJ system daal dunga aur sab galiyan sunenge",
    "Tere baap ka lund me DJ system daal dunga aur usme ad laga dunga",
    "Tere baap ka lund me DJ system daal dunga bina charger ke",
    "Tere baap ka lund me DJ system daal dunga bina data loss ke",
    "Tere baap ka lund me DJ system daal dunga bina reboot ke",
    "Tere baap ka lund me DJ system daal dunga fir usko chaat jaunga",
    "Tere baap ka lund me Discord server chala dunga bina data loss ke",
    "Tere baap ka lund me Discord server chala dunga bina permission ke",
    "Tere baap ka lund me Discord server chala dunga bina reboot ke",
    "Tere baap ka lund me Discord server chala dunga fir usko chaat jaunga",
    "Tere baap ka lund me Discord server chala dunga jise sab report karenge",
    "Tere baap ka lund me Notepad khol ke code likh dunga",
    "Tere baap ka lund me Notepad khol ke code likh dunga aur livestream chalu kar dunga",
    "Tere baap ka lund me Notepad khol ke code likh dunga bina data loss ke",
    "Tere baap ka lund me Notepad khol ke code likh dunga bina permission ke",
    "Tere baap ka lund me Notepad khol ke code likh dunga bina reboot ke",
    "Tere baap ka lund me Notepad khol ke code likh dunga fir usko chaat jaunga",
    "Tere baap ka lund me Notepad khol ke code likh dunga jise sab report karenge",
    "Tere baap ka lund me RAM stick daal dunga aur livestream chalu kar dunga",
    "Tere baap ka lund me RAM stick daal dunga aur usme ad laga dunga",
    "Tere baap ka lund me RAM stick daal dunga bina charger ke",
    "Tere baap ka lund me RAM stick daal dunga bina data loss ke",
    "Tere baap ka lund me RAM stick daal dunga bina permission ke",
    "Tere baap ka lund me RAM stick daal dunga bina reboot ke",
    "Tere baap ka lund me RAM stick daal dunga fir usko chaat jaunga",
    "Tere baap ka lund me RAM stick daal dunga jise sab report karenge",
    "Tere baap ka lund me SSD daal ke fast access kar lunga aur livestream chalu kar dunga",
    "Tere baap ka lund me SSD daal ke fast access kar lunga aur sab galiyan sunenge",
    "Tere baap ka lund me SSD daal ke fast access kar lunga bina charger ke",
    "Tere baap ka lund me SSD daal ke fast access kar lunga bina data loss ke",
    "Tere baap ka lund me SSD daal ke fast access kar lunga bina permission ke",
    "Tere baap ka lund me SSD daal ke fast access kar lunga fir usko chaat jaunga",
    "Tere baap ka lund me SSD daal ke fast access kar lunga jise sab report karenge",
    "Tere baap ka lund me firewall daal ke secure kar dunga",
    "Tere baap ka lund me firewall daal ke secure kar dunga aur livestream chalu kar dunga",
    "Tere baap ka lund me firewall daal ke secure kar dunga aur sab galiyan sunenge",
    "Tere baap ka lund me firewall daal ke secure kar dunga aur usme ad laga dunga",
    "Tere baap ka lund me firewall daal ke secure kar dunga bina charger ke",
    "Tere baap ka lund me firewall daal ke secure kar dunga bina data loss ke",
    "Tere baap ka lund me firewall daal ke secure kar dunga bina reboot ke",
    "Tere baap ka lund me firewall daal ke secure kar dunga fir usko chaat jaunga",
    "Tere baap ka lund me firewall daal ke secure kar dunga jise sab report karenge",
    "Tere baap ka lund me solar panel laga dunga aur livestream chalu kar dunga",
    "Tere baap ka lund me solar panel laga dunga bina charger ke",
    "Tere baap ka lund me solar panel laga dunga bina data loss ke",
    "Tere baap ka lund me solar panel laga dunga bina reboot ke",
    "Tere baap ka lund me spaghetti bana dunga",
    "Tere baap ka lund me spaghetti bana dunga aur livestream chalu kar dunga",
    "Tere baap ka lund me spaghetti bana dunga aur usme ad laga dunga",
    "Tere baap ka lund me spaghetti bana dunga bina charger ke",
    "Tere baap ka lund me spaghetti bana dunga bina data loss ke",
    "Tere baap ka lund me spaghetti bana dunga bina permission ke",
    "Tere baap ka lund me spaghetti bana dunga bina reboot ke",
    "Tere baap ka lund me spaghetti bana dunga fir usko chaat jaunga",
    "Tere baap ka lund me spaghetti bana dunga jise sab report ke aulad",
    "Tere baap ka lund pe GPS laga dunga bina permission ke",
    "Tere baap ka lund pe GPS laga dunga bina reboot ke",
    "Tere baap ka lund pe GPS laga dunga fir usko chaat jaunga",
    "Tere baap ka lund pe QR code chipka ke scan karwaunga aur livestream chalu kar dunga",
    "Tere baap ka lund pe QR code chipka ke scan karwaunga aur sab galiyan sunenge",
    "Tere baap ka lund pe QR code chipka ke scan karwaunga aur usme ad laga dunga",
    "Tere baap ka lund pe QR code chipka ke scan karwaunga bina charger ke",
    "Tere baap ka lund pe QR code chipka ke scan karwaunga bina data loss ke",
    "Tere baap ka lund pe QR code chipka ke scan karwaunga bina reboot ke",
    "Tere baap ka lund pe QR code chipka ke scan karwaunga fir usko chaat jaunga",
    "Tere baap ka lund pe QR code chipka ke scan karwaunga jise sab report karenge",
    "Tere baap ka lund pe barcode chipka dunga",
    "Tere baap ka lund pe barcode chipka dunga aur livestream chalu kar dunga",
    "Tere baap ka lund pe barcode chipka dunga aur sab galiyan sunenge",
    "Tere baap ka lund pe barcode chipka dunga aur usme ad laga dunga",
    "Tere baap ka lund pe barcode chipka dunga bina data loss ke",
    "Tere baap ka lund pe barcode chipka dunga bina permission ke",
    "Tere baap ka lund pe barcode chipka dunga fir usko chaat jaunga",
    "Tere baap ka lund pe barcode chipka dunga jise sab report karenge",
    "Tere baap ke mooch se violin bajake gali compose kar dunga aur sab galiyan sunenge",
    "Tere baap ke mooch se violin bajake gali compose kar dunga aur usme ad laga dunga",
    "Tere baap ke mooch se violin bajake gali compose kar dunga bina charger ke",
    "Tere baap ke mooch se violin bajake gali compose kar dunga bina data loss ke",
    "Tere baap ke mooch se violin bajake gali compose kar dunga bina reboot ke",
    "Tere baap ke mooch se violin bajake gali compose kar dunga fir usko chaat jaunga",
    "Tere baap ke mooch se violin bajake gali compose kar dunga jise sab report karenge",
    "Tere baap ko Flipkart pe sale pe daal dunga aur livestream chalu kar dunga",
    "Tere baap ko Flipkart pe sale pe daal dunga aur usme ad laga dunga",
    "Tere baap ko Flipkart pe sale pe daal dunga bina permission ke",
    "Tere baap ko Flipkart pe sale pe daal dunga bina reboot ke",
    "Tere baap ko Flipkart pe sale pe daal dunga fir usko chaat jaunga",
    "Tere baap ko Flipkart pe sale pe daal dunga jise sab report karenge",
    "Tere baap ko OnlyFans pe daal dunga",
    "Tere baap ko OnlyFans pe daal dunga aur livestream chalu kar dunga",
    "Tere baap ko OnlyFans pe daal dunga aur sab galiyan sunenge",
    "Tere baap ko OnlyFans pe daal dunga aur usme ad laga dunga",
    "Tere baap ko OnlyFans pe daal dunga bina charger ke",
    "Tere baap ko OnlyFans pe daal dunga bina permission ke",
    "Tere baap ko OnlyFans pe daal dunga bina reboot ke",
    "Tere baap ko OnlyFans pe daal dunga fir usko chaat jaunga",
    "Tere baap me AirPods daal ke gaane chala dunga",
    "Tere baap me AirPods daal ke gaane chala dunga aur livestream chalu kar dunga",
    "Tere baap me AirPods daal ke gaane chala dunga aur sab galiyan sunenge",
    "Tere baap me AirPods daal ke gaane chala dunga aur usme ad laga dunga",
    "Tere baap me AirPods daal ke gaane chala dunga bina permission ke",
    "Tere baap me AirPods daal ke gaane chala dunga jise sab report karenge",
    "Tere baap me Bluetooth speaker daal ke gali FM chala dunga aur livestream chalu kar dunga",
    "Tere baap me Bluetooth speaker daal ke gali FM chala dunga aur sab galiyan sunenge",
    "Tere baap me Bluetooth speaker daal ke gali FM chala dunga aur usme ad laga dunga",
    "Tere baap me Bluetooth speaker daal ke gali FM chala dunga bina charger ke",
    "Tere baap me Bluetooth speaker daal ke gali FM chala dunga bina data loss ke",
    "Tere baap me Bluetooth speaker daal ke gali FM chala dunga bina reboot ke",
    "Tere baap me Bluetooth speaker daal ke gali FM chala dunga fir usko chaat jaunga",
    "Tere baap me Bluetooth speaker daal ke gali FM chala dunga jise sab report karenge",
    "Tere baap me DJ system daal dunga",
    "Tere baap me DJ system daal dunga aur sab galiyan sunenge",
    "Tere baap me DJ system daal dunga aur usme ad laga dunga",
    "Tere baap me DJ system daal dunga bina data loss ke",
    "Tere baap me DJ system daal dunga bina reboot ke",
    "Tere baap me DJ system daal dunga fir usko chaat jaunga",
    "Tere baap me DJ system daal dunga jise sab report karenge",
    "Tere baap me Discord server chala dunga",
    "Tere baap me Discord server chala dunga aur livestream chalu kar dunga",
    "Tere baap me Discord server chala dunga aur sab galiyan sunenge",
    "Tere baap me Discord server chala dunga aur usme ad laga dunga",
    "Tere baap me Discord server chala dunga bina data loss ke",
    "Tere baap me Discord server chala dunga bina permission ke",
    "Tere baap me Discord server chala dunga jise sab report karenge",
    "Tere baap me Notepad khol ke code likh dunga",
    "Tere baap me Notepad khol ke code likh dunga aur sab galiyan sunenge",
    "Tere baap me Notepad khol ke code likh dunga aur usme ad laga dunga",
    "Tere baap me Notepad khol ke code likh dunga jise sab report karenge",
    "Tere baap me RAM stick daal dunga",
    "Tere baap me RAM stick daal dunga aur livestream chalu kar dunga",
    "Tere baap me RAM stick daal dunga aur sab galiyan sunenge",
    "Tere baap me RAM stick daal dunga aur usme ad laga dunga",
    "Tere baap me RAM stick daal dunga bina charger ke",
    "Tere baap me RAM stick daal dunga bina data loss ke",
    "Tere baap me RAM stick daal dunga bina reboot ke",
    "Tere baap me RAM stick daal dunga fir usko chaat jaunga",
    "Tere baap me RAM stick daal dunga jise sab report karenge",
    "Tere baap me SSD daal ke fast access kar lunga",
    "Tere baap me SSD daal ke fast access kar lunga aur livestream chalu kar dunga",
    "Tere baap me SSD daal ke fast access kar lunga aur sab galiyan sunenge",
    "Tere baap me SSD daal ke fast access kar lunga aur usme ad laga dunga",
    "Tere baap me SSD daal ke fast access kar lunga bina charger ke",
    "Tere baap me SSD daal ke fast access kar lunga bina data loss ke",
    "Tere baap me SSD daal ke fast access kar lunga bina permission ke",
    "Tere baap me SSD daal ke fast access kar lunga bina reboot ke",
    "Tere baap me SSD daal ke fast access kar lunga fir usko chaat jaunga",
    "Tere baap me SSD daal ke fast access kar lunga jise sab report karenge",
    "Tere baap me firewall daal ke secure kar dunga",
    "Tere baap me firewall daal ke secure kar dunga aur livestream chalu kar dunga",
    "Tere baap me firewall daal ke secure kar dunga aur sab galiyan sunenge",
    "Tere baap me firewall daal ke secure kar dunga aur usme ad laga dunga",
    "Tere baap me firewall daal ke secure kar dunga bina charger ke",
    "Tere baap me firewall daal ke secure kar dunga bina data loss ke",
    "Tere baap me firewall daal ke secure kar dunga bina reboot ke",
    "Tere baap me firewall daal ke secure kar dunga jise sab report karenge",
    "Tere baap me solar panel laga dunga aur usme ad laga dunga",
    "Tere baap me solar panel laga dunga bina charger ke",
    "Tere baap me solar panel laga dunga bina data loss ke",
    "Tere baap me solar panel laga dunga bina permission ke",
    "Tere baap me solar panel laga dunga jise sab report karenge",
    "Tere baap me spaghetti bana dunga",
    "Tere baap me spaghetti bana dunga aur livestream chalu kar dunga",
    "Tere baap hu bhosdiwale",

]

# --- Command Handlers ---

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message,
        "✨ 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙏𝙝𝙚 𝙐𝙡𝙩𝙞𝙢𝙖𝙩𝙚 𝙂𝙖𝙡𝙞 𝘽𝙤𝙩 ✨\n\n"
        "👑 Owner Commands:\n"
        "- /admin <user_id>\n"
        "- /remove_admin <user_id>\n"
        "- /list_admins\n\n"
        "🛡️ Admin Commands:\n"
        "- /approve <user_id>\n"
        "- /remove <user_id>\n"
        "- /remove_all\n"
        "- /list_approved\n\n"
        "🔥 User Commands:\n"
        "- /fuck <username>\n"
        "- /stop\n"
        "- /ping"
    )
    if message.from_user.id != owner_id:
        try:
            bot.send_message(owner_id, f"👤 {message.from_user.first_name} (@{message.from_user.username}) started the bot.")
        except:
            pass

@bot.message_handler(commands=["ping"])
def ping(message):
    start_time = time.time()
    sent = bot.reply_to(message, "Pinging...")
    end_time = time.time()
    latency = round((end_time - start_time) * 1000)
    bot.edit_message_text(f"🏓 Pong! {latency}ms", message.chat.id, sent.message_id)

# --- Owner Only ---

@bot.message_handler(commands=["admin"])
def make_admin(message):
    if message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only the owner can use this command.")
        return
    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "Usage: /admin <user_id>")
        return
    try:
        uid = int(parts[1])
        if uid not in admins:
            admins.append(uid)
            bot.reply_to(message, f"✅ User {uid} promoted to admin.")
        else:
            bot.reply_to(message, f"ℹ️ User {uid} is already an admin.")
    except:
        bot.reply_to(message, "❌ Invalid user ID.")

@bot.message_handler(commands=["remove_admin"])
def remove_admin(message):
    if message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only the owner can remove admins.")
        return
    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "Usage: /remove_admin <user_id>")
        return
    try:
        uid = int(parts[1])
        if uid == owner_id:
            bot.reply_to(message, "❌ You can't remove yourself (owner).")
            return
        if uid in admins:
            admins.remove(uid)
            bot.reply_to(message, f"✅ Admin {uid} removed.")
        else:
            bot.reply_to(message, "⚠️ User is not an admin.")
    except:
        bot.reply_to(message, "❌ Invalid user ID.")

@bot.message_handler(commands=["list_admins"])
def list_admins(message):
    if message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only the owner can view admins.")
        return
    if not admins:
        bot.reply_to(message, "📭 No admins found.")
        return
    reply = "👮 Admins:\n"
    for uid in admins:
        reply += f"- {uid}\n"
    bot.reply_to(message, reply)

# --- Admin Only ---

@bot.message_handler(commands=["approve"])
def approve_user(message):
    if message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only admins can approve users.")
        return
    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "Usage: /approve <user_id>")
        return
    try:
        uid = int(parts[1])
        username = f"user{uid}"
        for user in approved_users:
            if user['id'] == uid:
                bot.reply_to(message, "✅ User already approved.")
                return
        approved_users.append({'id': uid, 'username': username})
        save_approved_users()
        bot.reply_to(message, f"✅ Approved user {uid}")
    except:
        bot.reply_to(message, "❌ Invalid user ID.")

@bot.message_handler(commands=["remove"])
def remove_user(message):
    if message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only admins can remove users.")
        return
    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "Usage: /remove <user_id>")
        return
    try:
        uid = int(parts[1])
        for user in approved_users:
            if user['id'] == uid:
                approved_users.remove(user)
                save_approved_users()
                bot.reply_to(message, f"❌ Removed user {uid}")
                return
        bot.reply_to(message, "⚠️ User not found.")
    except:
        bot.reply_to(message, "❌ Invalid user ID.")

@bot.message_handler(commands=["remove_all"])
def remove_all_users(message):
    if message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only admins can clear approved users.")
        return
    approved_users.clear()
    save_approved_users()
    bot.reply_to(message, "🧹 All approved users removed.")

@bot.message_handler(commands=["list_approved"])
def list_approved(message):
    if message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only admins can view approved users.")
        return
    if not approved_users:
        bot.reply_to(message, "📭 No users are currently approved.")
        return
    reply = "✅ Approved Users:\n"
    for user in approved_users:
        reply += f"- {user['id']} (@{user['username']})\n"
    bot.reply_to(message, reply)

# --- Approved Users, Admins & Owner ---

@bot.message_handler(commands=["fuck"])
def send_all_galis(message):
    global stop_gali
    if message.from_user.id not in [u['id'] for u in approved_users] and message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 You are not approved to use this command.")
        return
    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "Usage: /fuck <username>")
        return
    username = parts[1]
    bot.reply_to(message, f"🔥 Starting gali spam for {username}...")

    def spam():
        while not stop_gali:
            random.shuffle(galis)
            for gali in galis:
                if stop_gali:
                    return
                try:
                    bot.send_message(message.chat.id, f"{username} {gali}")
                    time.sleep(0.3)
                except:
                    continue

    stop_gali = False
    for _ in range(3):
        t = threading.Thread(target=spam)
        t.daemon = True
        t.start()

@bot.message_handler(commands=["stop"])
def stop_galis(message):
    global stop_gali
    if message.from_user.id not in [u['id'] for u in approved_users] and message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 You are not approved to use this command.")
        return
    stop_gali = True
    bot.reply_to(message, "🛑 Stopping all galis...")

# --- Private Message Logger ---

@bot.message_handler(func=lambda msg: msg.chat.type == 'private')
def notify_owner_on_message(msg):
    if msg.from_user.id != owner_id:
        try:
            bot.send_message(owner_id, f"📩 Message from {msg.from_user.first_name} (@{msg.from_user.username}):\n{msg.text}")
        except:
            pass

# --- Start Polling ---
print("Bot is running...")
bot.infinity_polling()
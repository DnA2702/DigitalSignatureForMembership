from RSA import *
from SHA3 import *
from digitalSign import *

# Login Page
def Login():
    valid = False
    while (not(valid)):
        print("---Welcome, This is Login Page---")
        username = input("Username: ")
        password = input("Password: ")
        with open('akun.txt', 'r') as f:        
            akun_list = f.readlines()
            for i in range (len(akun_list)):
                akun = akun_list[i].split(',')
                if (akun[0] == username):
                    if ((akun[1].strip()) == password):
                        valid = True
                        return(username)
            print("Silahkan Masukkan Username dan Password yang Sesuai")
        
# Menu Page()
def Menu():
    print("---This is Main Page---")
    print("1. Channel")
    print("2. Profile")
    print("3. Logout")
    pilihan = input("Select Fitures: ")
    if (pilihan == "1"):
        Channel()
    elif (pilihan == "2"):
        Profile()
    elif (pilihan == "3"):
        print("Terima Kasih")

# Profile Page()
def Profile():
    print("---This is Your Profile Page---")
    print("Your Username: ", username)
    print("Press Zero to Back to the Menu")
    masukan = input()
    while(masukan != "0"):
        print("Press Zero to Back to the Menu")
        masukan = input()
    Menu()

def Channel():
    member = checkMembership()
    if member:
        pilihanChannelMember(member)
    else:
        pilihanChannelNonMember(member)
    
def checkMembership():
    membership = digitalSign(username)
    with open('channel.txt', 'r') as f:        
        membership_list = f.readlines()
        for i in range (len(membership_list)):
            if (membership_list[i] == membership):
                return True
    return False


def pilihanChannelMember(member):
    print("---Welcome To The Channel, Hope You Will Get Fun---")
    print("Enjoy Your Membership ", username, "<3")
    print("1. Video")
    print("2. Community")
    print("3. LiveStream")
    print("4. Discord")
    print("0. Menu")
    pilihan = input("Pick Features: ")
    if (pilihan == "1"):
        Video(member)
    elif (pilihan == "2"):
        Community(member)
    elif (pilihan == "3"):
        LiveStream(member)
    elif (pilihan == "4"):
        print("Join Our Discord Channel: https://discord.gg/kKAA6g3J")
        pilihanChannelMember(member)
    elif (pilihan == "0"):
        Menu()
    else:
        print("Masukkan Angka yang Sesuai!")
        pilihanChannelMember()

def pilihanChannelNonMember(member):
    print("---Welcome To The Channel, Hope You Will Get Fun---")
    print("1. Video")
    print("2. Community")
    print("3. LiveStream")
    print("0. Menu")
    pilihan = input("Pick Features: ")
    if (pilihan == "1"):
        Video(member)
    elif (pilihan == "2"):
        Community(member)
    elif (pilihan == "3"):
        LiveStream(member)
    elif (pilihan == "0"):
        Menu()
    else:
        print("Masukkan Angka yang Sesuai!")
        pilihanChannelNonMember()

def Video(member):
    if (member):
        print("---Enjoy the Video---")
        print("1. Vlog ke Jepang")
        print("2. Vlog ke Singapura")
        print("3. (Exclusive Content) Home Tour Bareng Istri")
        print("4. (Exlusice Content) Proses Pembelian Tiket ke Jepang biar Murah")
        print("0. Channel")
        pilihan = input("Masukan Pilihan: ")
        while(pilihan != "0"):
            pilihan = input("Masukan Pilihan: ")
        pilihanChannelMember(member)
    else:
        print("---Enjoy the Video---")
        print("1. Vlog ke Jepang")
        print("2. Vlog ke Singapura")
        pilihan = input("Masukan Pilihan: ")
        while(pilihan != "0"):
            pilihan = input("Masukan Pilihan: ")
        pilihanChannelNonMember(member)

def Community(member):
    if (member):
        print("Jangan Lupa Besok Bakal Ada GiveAway, So Stay Tuned!!!")
        print("(Exclusive Member) 27 Mei Gua Ultah, Ayo Meet & Greet!!!")
        print("Press Zero to Back to The Channel")
        pilihan = input()
        while(pilihan != "0"):
            pilihan = input()
        pilihanChannelMember(member)
    else:
        print("Jangan Lupa Besok Bakal Ada GiveAway, So Stay Tuned!!!")
        print("Press Zero to Back to The Channel")
        pilihan = input()
        while(pilihan != "0"):
            pilihan = input()
        pilihanChannelNonMember(member)
        
def LiveStream(member):
    if (member):
        print("1. (Exclusive Member) Nyubuh Bareng Tamatin Flappy Bird")
        print("2. (Exclusive Member) (Tayangan Ulang) Nunggu Magrib Main PUBG")
        print("3. (Exclusive Member) (Tayangan Ulang) Iseng Live Stream Makan Ramen di Jepang")
        print("0. Channel")
        pilihan = input("Masukan Pilihan: ")
        while(pilihan != "0"):
            pilihan = input()
        pilihanChannelMember(member)
    else:
        print("Maaf Lagi Ga Ada LiveStream, Boleh Dicek Video Lain Yaaa")
        print("Press Zero to Back to The Channel")
        pilihan = input()
        while(pilihan != "0"):
            pilihan = input()
        pilihanChannelNonMember(member)

# Main Program
username = Login()
Menu()
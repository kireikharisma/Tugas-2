dftr_nama = []
dftr_no_telp = []

def tambah_kontak():
    jawab = "y"
    while jawab=="y" :
        nama = input("- Nama    : ")
        no_telp = int(input("  No telp : (+62)"))
        dftr_nama.append(nama)
        dftr_no_telp.append(no_telp)
        print("Kontak berhasil ditambahkan")
        jawab=input("Pilih y/n : ")
        if jawab=="y":
            pass
        elif jawab=="n":
            return dftr_nama, str(dftr_no_telp)
        else :
            print("Pilihan tidak tersedia, hanya menerima masukan pilihan y atau n saja")
        
def dftr_kontak():
    x=0
    while x < len(dftr_nama) :
        print(str(x+1) + ". Nama       : " + str(dftr_nama[x]))
        print("   No Telepon : (+62)"+ str(dftr_no_telp[x]))
        x+=1

while True : 
    print("====================================================")
    print("+---------------- Selamat Datang! -----------------+")
    print("+---\t\t   --- Menu ---   \t\t---+")
    print("+---\t\t 1. Daftar Kontak \t\t---+")
    print("+---\t\t 2. Tambah Kontak \t\t---+")
    print("+---\t\t 3. Keluar \t\t\t---+")
    pil_menu= int(input("Pilih menu(1/2/3) : "))
    print("====================================================")
    if pil_menu==1 :
        print("Daftar Kontak :")
        dftr_kontak()
    elif pil_menu==2 :
        print("Masukkan Data :")
        tambah_kontak()
        
    elif pil_menu==3 :
        print("Program selesai, sampai jumpa!")
        break 
    else :
        print("Menu tidak tersedia")   
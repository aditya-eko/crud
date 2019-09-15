mahasiswa=[]

def tambah():
    masukan=str(input("masukan nama mahasiswa: "))
    global mahasiswa
    # mahasiswa=[]
    mahasiswa+=[masukan]
    return masukan


def kurang():
    masukan=str(input("masukan nama yang akan di hapus: "))
    global mahasiswa
    mahasiswa.remove(masukan)
    return mahasiswa


def edit():
    masukan=str(input("nama yang akan di edit: "))
    masukan2=str(input("masukan nama baru: "))
    global mahasiswa
    masukan2=mahasiswa.append(masukan2)
    return mahasiswa


# menambah dengan fungsi
print(mahasiswa)
tambah()
print(mahasiswa)
tambah()
print(mahasiswa)



# mengurangi mahasiswa dengan fungsi

kurang()
print(mahasiswa)

edit()
print(mahasiswa)
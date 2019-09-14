mahasiswa=["eko","agus"]

def tambah(up):
    return mahasiswa.insert(9,up)

def kurang(up):
    return mahasiswa.pop(up)


def edit(up):
    mahasiswa[0]=up
    return mahasiswa

def tampil():
    for i in (mahasiswa):
        print("nama mahasiswa adalah",i)


# menambahkan item dengan menggunakan fungsi
tambah("aditya")
print(mahasiswa)
print(mahasiswa.index("eko"))


# mengurangi item dengan fungsi
kurang(1)
print(mahasiswa)

# edit dengan menggunakan fungsi

edit("aldi")
print(mahasiswa)

# menampilkan mahasiswa

tampil()

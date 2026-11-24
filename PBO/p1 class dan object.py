class Alfamart:
    pass
class Kasir:
    pass

alfamart1 = Alfamart()
alfamart2 = Alfamart()
print(type(alfamart1))
print(type(alfamart2))

kasir1 = Kasir()
kasir2 = Kasir()
print(type(kasir1))
print(type(kasir2))

alfamart1 = Alfamart()
alfamart1.id = 12345
alfamart1.nama = "Alfamart Cibinong"
print(alfamart1.id)
print(alfamart1.nama)

alfamart2 = Alfamart()
alfamart2.id = 54321
alfamart2.nama = "Alfamart Bogor"
print(alfamart2.id)
print(alfamart2.nama)

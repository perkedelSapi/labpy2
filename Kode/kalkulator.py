bilangan=float(input('masukkan angka:'))

bilangan2=float(input('masukkan angka:'))
operasi=input('pilih operasi +,-,*,/:')


if operasi =='-':
    hasil= bilangan - bilangan2
    print('hasil:', hasil)
elif operasi =='+':
    hasil= bilangan + bilangan2
    print('hasil:', hasil)
elif operasi =='*':
    hasil= bilangan * bilangan2
    print('hasil:', hasil)
elif operasi =='/':
   if bilangan2 !=0:
    hasil= bilangan / bilangan2
    print('hasil:', hasil)
   else:
      print('tidak bisa dibagi dengan 0')
else:
   print('operasi tidak valid')

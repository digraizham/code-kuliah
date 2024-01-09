import bpy
from math import sin, pi

merah = bpy.data.objects['merah']
biru = bpy.data.objects['biru']
hijau = bpy.data.objects['hijau']

frame_number = 0

for i in range(0, 101):
    
    bpy.context.scene.frame_set(frame_number)  
    
    # animasi untuk kubus merah
    # kubus merah bergerak sesuai dengan fungsi sinus
    # dengan y = sin(x) dan nilai z tidak berubah, yaitu 0
    xmerah = i/2 * pi
    # dikalikan 10 supaya lokasi y lebih jauh
    ymerah = sin(xmerah) * 10
    zmerah = 0    
    
    merah.location = (xmerah, ymerah, zmerah)
    merah.keyframe_insert(data_path='location', index=-1)
    
    # animasi untuk kubus biru
    # kubus biru tidak hanya menganimasikan di sumbu y
    # tetapi juga di sumbu z, dengan z = sin(x)
    xbiru = i/3 * pi
    ybiru = 10 + sin(xbiru) * 5    # ditambah 10 karena titik awal
    zbiru = sin(xbiru) * 10  
    
    biru.location = (xbiru, ybiru, zbiru)
    biru.keyframe_insert(data_path='location', index=-1)
    
    # animasi kubus hijau
    # pada animasi ini pergerakannya ada di sumbu Y
    # dimana fungsi animasinya adalah x = sin(y)
    yhijau =  i/4 * pi + 20            # ditambah 20 karena titik awal
    xhijau = sin(yhijau - 20) * 5      # nilai y kembali dikurangi 20
    zhijau = 0 
    
    hijau.location = (xhijau, yhijau, zhijau)
    hijau.keyframe_insert(data_path='location', index=-1)    
    
    frame_number += 5

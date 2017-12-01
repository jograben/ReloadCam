#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ReloadCamUndro():
   # Read in the file
   with open(cccamPath, 'r') as file :
      
      # Replace the target string 
      lines = [( '' + line.replace('C: ', 'C:').replace('|1|0', '').replace('DEFAULT:1', '#').replace('DEFAULT:0', '#').replace(' ', '|').rstrip('\n') + '|1|0' + "\n" ) for line in open(cccamPath) ]

   # Write the file out again
   with open(cccamPath, 'w') as file: 
   
      #IKS
      if lines == 0:
         file.write('DEFAULT:1\n')
      #CCCAM
      file.writelines(lines)


   import time
   # Reinicio de Spring.apk (al salir de qpython cargará de nuevo listas, canales, ...)
   #os.system("adb shell am force-stop com.dvb.spring.home")
   # Se copia el archivo al sistema
   os.system("adb push " + ReloadCam.cccamPath + " /data/data/com.dvb.spring.home/app_tmp/card_server.cfg")
   
   print "Saliendo ..."
   
   # Salimos de qpython
   time.sleep(1.5)
   os.system("adb shell am force-stop com.hipipal.qpyplus")

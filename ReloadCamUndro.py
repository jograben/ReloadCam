#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ReloadCam

def GetVersion():
   return 1

def ReloadCamUndro():
   import os
   
   lines = []
   
   # Read in the file
   with open(ReloadCam.cccamPath, 'r') as file:
      # Replace the target string 
      print ("\n \tcard_server.cfg: \n")
      import ReloadCam_CCcamTester
      
      for line in file:
      	#print ("\t" + line)
      	if ReloadCam_CCcamTester.TestCline(line):
      		myLine = '' + line.replace('C: ', 'C:').replace('N: ', 'N:').replace('01 02 03 04 05 06 07 08 09 10 11 12 13 14', '01-02-03-04-05-06-07-08-09-10-11-12-13-14').replace('|1|0', '').replace('DEFAULT:1', '#').replace('DEFAULT:0', '#').replace(' ', '|').replace(' ', '|').replace('||', '|').rstrip('\n') + '|1|0' + "\n"

      		if not myLine.startswith('#'):
      			lines.append( myLine )

   # Write the file out again
   with open(ReloadCam.cccamPath, 'w') as file:
   
      #IKS
      if len(lines) == 0:
         file.write('DEFAULT:0\n')
      #CCCAM
      file.writelines(lines)

   import time
   # Reinicio de Spring.apk (al salir de qpython cargará de nuevo listas, canales, ...)
   #os.system("adb shell am force-stop com.dvb.spring.home")
   import shutil
   shutil.copy2(ReloadCam.cccamPath, ReloadCam.cccamBin)
   
   print "\nSaliendo ..."
   
   # Salimos de qpython
   time.sleep(1.2)
   os.system("adb shell am force-stop com.hipipal.qpyplus")

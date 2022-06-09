import pipes
import time
import signal
import os
t = pipes.Template()
#t.append()
#f = t.open('pipeT1toT2', 'w')
PID=str(os.getpid())
os.system ("clear")
Evento='0'
reintento=0
#Manejo de PID

PIDs=[0,0,0,0]

#interfaz de salida
# 0 PID propio
# 1 PID Interfaz de salida
# 2 PID Interfaz de sonido BACKGROUND


#*************************************
#Tuberias comunicacion entre Main e interfaz salida
print("Constructor de Tuberias")

f = t.open('Tuberia/pipeT1toT2', 'w') #Envio PID de Main a Interfaz de salida
f.write("")#Limpio tuberia
f.close()

f2=t.open('Tuberia/pipeT2toT1', 'w') #Envio PID de Interfaz de salida a Main
f2.write("")#Limpio tuberia
f2.close()

f3 = t.open('Tuberia/DatoMtoIo', 'w') #Envio Evento a interfaz de salida
f3.write("")#Limpio tuberia
f3.close()

f4 = t.open('Tuberia/BgMtoIo', 'w') #Envio BACKGROUND a interfaz de salida
f4.write("")#Limpio tuberia
f4.close()

f5 = t.open('Tuberia/PipeMtoIsbg', 'w') #Envio PID de Main a Interfaz de sonido BG
f5.write("")#Limpio tuberia
f5.close()

f6 = t.open('Tuberia/PipeIsbgtoM', 'w') #Envio PID de Main a Interfaz de sonido BG
f6.write("")#Limpio tuberia
f6.close()


f6 = t.open('Tuberia/DatoMtoIsbg', 'w') #Envio PID de Main a Interfaz de sonido BG
f6.write("")#Limpio tuberia
f6.close()


print("Tuberias construidas")
#*************************************

print("""
MAIN
Version 1,0
Fecha 23/12/2021
Auror Ingeniero Marcelo Casazza
""")
time.sleep(2)
while True:
	
	print(""" 
*********************MAIN***************************
EStablecer comunicacion
0- Envio mi PID a TUBERIA: Interfaz de salida y SOnido BG
1- Leer PID de INTERFAZ de salida
2- Leer PID deInterfaz de sonido BG

****************************************************
Programa


100 -Enviar señal a interfaz de salida Evento1
101 -Enviar señal a interfaz de salida Evento2

200 -Enviar señal a interfaz de salida BGROUND

300 -Enviar señal sonido a interfaz de sonido BGROUND
301 -Enviar señal sonido a interfaz de sonido BGROUND

400- Evento1
q- Salir
	
	""")

	Evento=input()
	
	if Evento=='0':
		#Envio PID a interfaz de salida	
		print("Enviando PID a otras interfaces")
		PIDs[0]=os.getpid()
		PID=str(os.getpid())
		print("PID de proceso MAIN",PID)
		f = t.open('Tuberia/pipeT1toT2', 'w')
		f.write(PID)#escribo PID en tuberia
		f.close()
		
		#Envio PID a interfaz de sonido BG
		f = t.open('Tuberia/PipeMtoIsbg', 'w')
		f.write(PID)#escribo PID en tuberia
		f.close()
		time.sleep(2)
	
	if Evento=='1':
		print("Leyeondo PID de interfaz de salida")
		#f2=t.open('Tuberia/pipeT2toT1', 'w')
		PIDsalida=open('Tuberia/pipeT2toT1').read()
		#f2.close()
		if PIDsalida=='':
			
			reintento=reintento+1
			print("Tuberia no creada aun, reintentando",reintento)
			time.sleep(2)
			
		else:
			print("Tuberia creada")
			PIDs[1]=int(PIDsalida)
			print("PID de INTERFAZ DE SALIDA",PIDs[1])
			time.sleep(2)
			#Evento='q'


	if Evento=='2':
		print("Leyendo PID de interfaz de sonidoBG")
		#f2=t.open('Tuberia/PipeIsbgtoM', 'w')
		PIDsalida=open('Tuberia/PipeIsbgtoM').read()
		#f2.close()
		if PIDsalida=='':
			
			reintento=reintento+1
			print("Tuberia Interfaz de sonido BG no creada aun, reintentando",reintento)
			time.sleep(2)
			
		else:
			print("Tuberia Interfaz de sonido BG creada")
			PIDs[2]=int(PIDsalida)
			print("PID de Interfaz de sonido BG",PIDs[2])
			time.sleep(2)




	if Evento=='100':
		print("Envio de señales al proceco PID", PIDs[1])
		
		f3 = t.open('Tuberia/DatoMtoIo', 'w')
		f3.write('Evento1')#escribo PID en tuberia
		f3.close()
		os.kill(PIDs[1], signal.SIGUSR1)
		
	
	if Evento=='101':
		print("Envio de señales al proceco PID", PIDs[1])
		
		f3 = t.open('Tuberia/DatoMtoIo', 'w')
		f3.write('Evento2')#escribo PID en tuberia
		f3.close()
		os.kill(PIDs[1], signal.SIGUSR1)
		
	if Evento=='200':
		print("Envio de nuevo archivo de salida, proceco PID", PIDs[1])
		
		f4 = t.open('Tuberia/BgMtoIo', 'w')
		f4.write('Bground1')#escribo PID en tuberia
		f4.close()
		#os.kill(PIDsalida, signal.SIGUSR1)

	if Evento=='300':
		print("Envio de nuevo archivo de salida, proceco PID", PIDsalida)
		
		f4 = t.open('Tuberia/DatoMtoIsbg', 'w')
		f4.write('Intro4')#escribo PID en tuberia
		f4.close()
	if Evento=='301':
                print("Envio de nuevo archivo de salida, proceco PID", PIDs[2])

                f4 = t.open('Tuberia/DatoMtoIsbg', 'w')
                f4.write('Intro3')#escribo PID en tuberia
                f4.close()
	
	if Evento=='400':
                print("Envio de nuevo archivo de salida, proceco PID", PIDs[2])

                f4 = t.open('Tuberia/DatoMtoIsbg', 'w')
                f4.write('Evento1')#escribo PID en tuberia
                f4.close()


	
	
	if Evento=='q':
		print("SALIR")
		f = t.open('Tuberia/pipeT1toT2', 'w')
		f.write("")#Limpio tuberia
		f.close()
		f2=t.open('Tuberia/pipeT2toT1', 'w')
		f2.write("")#Limpio tuberia
		f2.close()
	
		break

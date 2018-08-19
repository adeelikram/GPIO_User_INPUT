#use board sheme of gpio.board
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
i=0
print(" GPIO mode Board scheme")
print("\t1 2\n\t3 4\n\t5 6")
print("   GPIO 7 8\n\t9 10\n  GPIO 11 12 GPIO\n       13 14\n  GPIO 15 16 GPIO")
print("       17 18 GPIO\n  GPIO 19 20\n")
#sentinaled contrlloed loop for user inputt

while i==0: 
   print("1.Led 1 on\n2.Led 2 on\n3.Led 3 on\n4.Led 4 on\n5.close desired led\n6.exit")
   c=int(input("Enter your choice:"))
   p=0
   if c==1:
       GPIO.output(11,True)
       
   elif c==2:
       GPIO.output(12,True)

   elif c==3:
       GPIO.output(16,True)

   elif c==4:
       GPIO.output(18,True)

   elif c==5:
        while p==0: 
            print("1.Led 1 off\2.Led 2 off\n3.Led 3 off\n4.Led 4 off\n5.exit")
            c=int(input("Enter your choice:"))
            if c==1:
               GPIO.output(11,False)
       
            elif c==2:
               GPIO.output(12,False)

            elif c==3:
               GPIO.output(16,False)

            elif c==4:
               GPIO.output(18,False)
            elif c==5:
                p+=1
   elif c==6:
        i+=1
   else:
       print("Wrong input try again")

GPIO.cleanup()

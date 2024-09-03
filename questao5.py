def descobrir_interruptores():
    interruptores = [False, False, False]
    
    interruptores[0] = True
    print("Ligue o primeiro interruptor e espere alguns minutos.")
    
    interruptores[0] = False
    interruptores[1] = True
    print("Desligue o primeiro interruptor e ligue o segundo interruptor.")
    
    print("Vá até a sala das lâmpadas e verifique:")
    print("1. Qual lâmpada está acesa.")
    print("2. Qual lâmpada está apagada e quente.")
    print("3. Qual lâmpada está apagada e fria.")
    
    print("A lâmpada que está acesa é controlada pelo segundo interruptor.")
    print("A lâmpada que está apagada e quente é controlada pelo primeiro interruptor.")
    print("A lâmpada que está apagada e fria é controlada pelo terceiro interruptor.")

descobrir_interruptores()

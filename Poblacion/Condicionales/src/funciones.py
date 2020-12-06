def Bisiesto(anyo):
    if anyo%4 == 0:
        print("Es Bisiesto")
        return True
    else:
        print("No es Bisiesto")
        return False

def fechas(dia, mes, anyo):
    if (anyo>=0):


        if((mes%2 == 0) and (0<mes<=12)):
            if(mes== 7):
                
            if 0<dia<=30:
                print("esta bien la fecha")
            else:
                print("esta mal el dia o mes")
            if 0<dia<=31:
                print("esta bien la fecha")
            else:
                print("esta mal el dia o mes")
        elif 0<mes<=12:
            if 0<dia<=30:
                print("esta bien la fecha")
            else:
                print("esta mal el dia o mes")
    else:
        print("hola")

    
        
    
        

fechas(31,9,2018)

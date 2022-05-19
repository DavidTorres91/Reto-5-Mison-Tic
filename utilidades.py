import re

def vtipo_doc(tipo_doc ):
  if(tipo_doc == 'CC' or
     tipo_doc == 'TI' or 
     tipo_doc == 'PA' or 
     tipo_doc == 'CE'):
       return True
  else:
    False

def vnumero_doc(numero_doc):
  if(numero_doc.isnumeric() and len(numero_doc) <= 12):
    return True
  else:
    False

def nombre(vnombre):
  if(nombre.isalpha() and len(nombre)<=30):
    return True
  else:
    False

def vapellido(apellido):
  if(apellido.isalpha() and len(nombre)<=30):
    return True
  else:
    False

def vfecha(fecha):
  if(len(fecha)<=10):
    return True
  else:
    False

def vrh_gs(rh_gs):
  if(rh_gs[0]=="O" or rh_gs[0]=="A" or rh_gs[0]=="B")and(rh_gs[1] == "+" or rh_gs[1] == "-"):
    return True
  else:
    False

def vcorreo(correo):
  if(len(correo)<=50 and
     re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,3}$',correo.lower())):
    return True
  else:
    False

def vnumero_tel(numero_tel):
  if(len(numero_tel) <11 and numero_tel.isnumeric()):
    return True
  else:
    False






    


















"""
def ():
  if():
    return True
  else:
    False

def ():
  if():
    return True
  else:
    False

def ():
  if():
    return True
  else:
    False

def ():
  if():
    return True
  else:
    False"""
import re,datetime


def vtipo_doc(tipo_doc ):
  if(tipo_doc == 'CC' or
     tipo_doc == 'TI' or 
     tipo_doc == 'PA' or 
     tipo_doc == 'CE'):
       return True
  else:
    return False

def vnumero_doc(numero_doc):
  if(numero_doc.isnumeric() and len(numero_doc) <= 12):
    return True
  else:
    return False

def vnombre(nombre):
  if(nombre.isalpha() and len(nombre)<=30):
    return True
  else:
    return False

def vapellido(apellido):
  if(apellido.isalpha() and len(apellido)<=30):
    return True
  else:
    return False

def vfecha(fecha):
  if(len(fecha)<=10):
    return True
  else:
    return False

def vrh_gs(rh_gs):
  if (len(rh_gs)==2):
    if  (rh_gs[0]=="O" or rh_gs[0]=="A" or rh_gs[0]=="B")and(rh_gs[1] == "+" or rh_gs[1] == "-"):
      return True
    else:
      return False
  else:
    return False

def vcorreo(correo):
  if(len(correo)<=50 and
     re.match('^[(a-z0-9\_\-\.)]{3,10}@[(a-z0-9\_\-)]{3,}\.[(a-z)]{2,3}$',correo.lower())):
    return True
  else:
    return False
def vnumero_tel(numero_tel):
  if(len(numero_tel) <11 and numero_tel.isnumeric()):
    return True
  else:
    return False

def validar_usuario(tipo_doc,numero_doc,nombre,apellido,fecha,rh_gs,correo,numero_tel):
  if (tipo_doc() and
      numero_doc() and
      nombre() and
      apellido() and
      fecha() and
      rh_gs() and
      correo() and
      numero_tel()):
        return True
  else:
    return False

def crear_persona(tipo_doc,numero_doc,nombre,apellido,fecha,rh_gs,correo,numero_tel):
  persona = {
  'Tipo doccumento' : tipo_doc,
  'numero_doc' : numero_doc,
  'nombre' : nombre,
  'apellido' : apellido,
  'fecha_nacio' : fecha,
  'rh_gs' : rh_gs,
  'correo' : correo,
  'numero_tel' : numero_tel 
}
  
  return persona




def Validar_Existente(numero_documento, personas):
    for persona in personas:
        if persona['Numero de documento'] == numero_documento:
          print("Ya esta registrado")
          return True
        else:
          print("No esta registrado")
          return False 



def validar_fecha_cita(fecha_cita):
    if datetime.strptime(fecha_cita, '%Y-%m-%d') > datetime.now():
        return True
    else:
        return False
"""
def ():
  if():
    return True
  else:
    False"""

def agendar_citas(personas,numero_doc,fecha):
  existe=Validar_Existente(personas,numero_doc) 
  if existe :

    fecha_date = datetime.strptime(fecha, '%Y-%m-%d').date()
    if validar_fecha_cita(fecha_date):
      return fecha_date
  else:
    return False

def visualizar_usuarios(tipo_doc,numero_doc,nombre,apellido,fecha,rh_gs,correo,numero_tel):

  vista = print(f"""\n  -*-*-*-*-*-*-*-*-*-*-*-  
  | Tipo de Doc.\t | {tipo_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-  
  | Numero de Doc.\t | {numero_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Nombre.\t | {nombre} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Apellido.\t | {apellido} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Fecha de Nacimiento.\t | {fecha} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Tipo de sangre.\t | {rh_gs[0]} {rh_gs[1]} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Correo.\t | {correo} |
  -*-*-*-*-*-*-*-*-*-*-*-
  | número.\t | {numero_tel} |                  
  -*-*-*-*-*-*-*-*-*-*-*-\n""")
  return vista
############################################# Primera instancia #############################################
import pandas as pd

if __name__ == '__main__':
    # Datos del programa #
    ipc = {
        'Marzo': 0,
        'Abril': 0,
        'Mayo': 0,
        'Junio': 0,
        'Julio': 0
    }
    
    rem = {
        'Marzo': 15.3,
        'Abril': 13,
        'Mayo': 10,
        'Junio': 8.2,
        'Julio': 8
    }
    
    mep = {
        'Marzo': 15.3,
        'Abril': 0,
        'Mayo': 0,
        'Junio': 0,
        'Julio': 0
    }

    alquiler = 280000
    meses = [ipc.keys]
    datos = [rem.values(), ipc.values(), mep.values()]
    meses = rem.keys()
    indice = ['Rem (%)', 'IPC (%)', 'MEP ($)']
    tabla = pd.DataFrame(data=datos, index=indice, columns= meses
                         
    print(tabla)

  #### Tabla variaciones ###

  meses_alquiler = []
    
  for x in meses: # Se separan los meses de la tupla.
    meses_alquiler.append(x)

    meses_alquiler.append('Agosto')
    meses_alquiler.remove('Marzo')

    alquiler_rem = {}
    alquiler_ipc = None
    alquiler_mep = None

    for k,v in rem.items(): # Se agregan datos al diccionario 
        monto_alquiler = alquiler
        contador_mes = 0
        valor_ajustado =alquiler_rem[meses_alquiler[0]]= monto_alquiler * ((1+v)/100)
        monto_alquiler = valor_ajustado
        print(monto_alquiler)
         
    tabla_alquiler = 
      
    print(meses_alquiler)

############################################# Primera instancia #############################################
import pandas as pd

##### Funciones #####


def calcular_ajuste_inflacion(alquiler, **iterador):
    monto_alquiler = alquiler
    contador_mes = 0
    monto_ajustado = {}
  
    for k, v in iterador.items():
      valor_ajustado = monto_alquiler * (1 + (v / 100))
      monto_alquiler = round(valor_ajustado, 2)
      monto_ajustado[meses_alquiler[contador_mes]] = {monto_alquiler}
      contador_mes += 1
  
    return monto_ajustado


def calcular_ajuste_usd(variable_rem, **iterador):

    contador_mes = 0
    monto_ajustado = {}
    lista = []
  
    for x, y in variable_rem.items():
      lista.append(int(y))
  
    for k, v in iterador.items():
      print(lista[contador_mes])
      print(v)
  
      valor_ajustado = variable_rem[k] / (v)
      monto_alquiler = round(valor_ajustado, 2)
      monto_ajustado[meses_alquiler[contador_mes]] = f'${monto_alquiler}'
      contador_mes += 1
  
    return monto_ajustado


if __name__ == '__main__':
  # Datos del programa #
  ipc = {'Marzo': 0, 'Abril': 0, 'Mayo': 0, 'Junio': 0, 'Julio': 0}
  
  rem = {'Marzo': 15.3, 'Abril': 13, 'Mayo': 10, 'Junio': 8.2, 'Julio': 8}
  
  mep = {
      'Abril': 1053,
      'Mayo': 1074.06,
      'Junio': 1095.04,
      'Julio': 1117.45,
      'Agosto': 1139.80
  }
  
  alquiler = 280000
  meses = [ipc.keys]
  datos = [rem.values(), ipc.values(), mep.values()]
  meses = rem.keys()
  indice = ['Rem (%)', 'IPC (%)', 'MEP ($)']
  tabla = pd.DataFrame(data=datos, index=indice, columns=meses)
  
  print(tabla)
  #### Tabla variaciones ###
  
  meses_alquiler = []

  for x in meses:  # Se separan los meses de la tupla.
    meses_alquiler.append(x)

  meses_alquiler.append('Agosto')
  meses_alquiler.remove('Marzo')

  alquiler_rem = calcular_ajuste_inflacion(alquiler, **rem)
  alquiler_ipc = calcular_ajuste_inflacion(alquiler, **ipc)
  alquiler_mep = calcular_ajuste_usd(alquiler_rem, **mep)
  """
    monto_alquiler = alquiler
    contador_mes = 0
    """
  indice_ajuste = ['Aj REM', 'Aj IPC', 'Aj MEP']
  """
    # Se realiza ajuste por REM y se agregan datos al diccionario
    for k, v in rem.items():
        valor_ajustado = monto_alquiler * (1 + (v / 100))
        monto_alquiler = round(valor_ajustado, 2)
        alquiler_rem[meses_alquiler[contador_mes]] = f'${monto_alquiler}'
        contador_mes += 1
    """
  datos_ajustados = [
      alquiler_rem.values(),
      alquiler_ipc.values(),
      alquiler_mep.values()
  ]
  tabla_ajustada = pd.DataFrame(data=datos_ajustados,
                                index=indice_ajuste,
                                columns=meses_alquiler)

  print(tabla_ajustada)

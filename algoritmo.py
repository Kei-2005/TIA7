import random
import pandas as pd
from datetime import datetime, timedelta


def generar_datos_lecturas(n=20):
    datos = []
    fecha_base = datetime.now()
    sensores = ["A1S01", "A2S05", "B3S09", "C1S02"]
    microcontroladores = ["A1M01", "A2M05", "B3M09", "C1M02"]
    lineas = ["A1", "A2", "B3", "C1"]
    fabricas = ["A", "B", "C"]
    
    for i in range(n):
        fecha = (fecha_base - timedelta(seconds=i*10)).date().isoformat()
        hora = (fecha_base - timedelta(seconds=i*10)).time().strftime("%H:%M:%S")
        sensor_id = random.choice(sensores)
        micro_id = random.choice(microcontroladores)
        linea = random.choice(lineas)
        fabrica = random.choice(fabricas)
        concentracion = round(random.uniform(0.1, 600.0), 2)
        
        if concentracion <= 0.5:
            nivel = "Exposición leve"
        elif concentracion <= 1:
            nivel = "Exposición permitida"
        elif concentracion <= 10:
            nivel = "Moderada toxicidad"
        elif concentracion <= 50:
            nivel = "Peligroso"
        elif concentracion <= 500:
            nivel = "Altamente peligroso"
        else:
            nivel = "Peligro extremo"
        
        latitud = round(random.uniform(6.2, 6.3), 6)
        longitud = round(random.uniform(-75.6, -75.5), 6)
        
        datos.append([fecha, hora, sensor_id, micro_id, linea, fabrica,
                      concentracion, nivel, latitud, longitud])
        
    df = pd.DataFrame(datos, columns=[
        "Fecha", "Hora", "Sensor_ID", "Microcontrolador_ID", "Linea_Produccion", 
        "Fabrica", "Concentracion_ppm", "Nivel_Riesgo", "Latitud", "Longitud"
    ])
    
    print(df)
    df.to_excel("lecturas_sensor.xlsx", index=False)
    print("\nArchivo 'lecturas_sensor.xlsx' generado con éxito.")


generar_datos_lecturas(20)
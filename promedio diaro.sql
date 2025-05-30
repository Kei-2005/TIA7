SELECT 
  f.nombre_fabrica AS fabrica,
  l.fecha,
  ROUND(AVG(l.ppm), 2) AS promedio_ppm
FROM lectura l
JOIN sensor s ON l.id_sensor = s.id_sensor
JOIN microcontrolador m ON s.id_micro = m.id_micro
JOIN linea_produccion lp ON m.id_linea = lp.id_linea
JOIN fabrica f ON lp.id_fabrica = f.id_fabrica
GROUP BY f.nombre_fabrica, l.fecha
ORDER BY l.fecha;

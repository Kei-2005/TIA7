SELECT 
  s.id_sensor,
  ROUND(AVG(l.ppm), 2) AS promedio_ppm
FROM lectura l
JOIN sensor s ON l.id_sensor = s.id_sensor
GROUP BY s.id_sensor
ORDER BY promedio_ppm DESC
LIMIT 15;

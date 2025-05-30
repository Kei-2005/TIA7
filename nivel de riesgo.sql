SELECT 
  nivel_riesgo,
  COUNT(*) AS cantidad
FROM lectura
GROUP BY nivel_riesgo
ORDER BY cantidad DESC;

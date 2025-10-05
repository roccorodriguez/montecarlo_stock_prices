# Monte Carlo Simulation Stock Prices

Este repositorio provee un dashboard interactivo que permite visualizar los resultados de una simulación de Monte arlo para la proyección futura del precio de una acción. El dashboard está diseñado para ser amigable e interactivo, permitiendo a los usuarios elegir la acción a analizar y explorar cómo cambios en el drift y en otros parámetros modifican los resultados finales.

https://blackschole.streamlit.app/

## 🚀 Funcionalidades:

1. **Visualización de los resultados de la simulación**: 
   - Se visualiza la evolución simultánea de las distintas simulaciones de precios mediante un gráfico de líneas.
   - Se visualiza la distribución de los precios finales mediante un histograma.
   
2. **Dashboard interactivo**:
   - El dashboard permite actualizar los parámetros de la simulación de manera interactiva.
   - Los usuarios pueden ingresar diferentes acciones, modificar el alcance y número de simulaciones, y personalizar el drift para observar cómo afectan estos cambios a los resultados finales.
   - La simulación se ejecuta automáticamente al ingresar los parámetros y se muestran los resultados en tiempo real.
   
3. **Información estadística**:
   - Se proporcionan estadísticas básicas como precios mínimos y máximos, percentiles 10 y 90, así como probabilidades de ganancia y de pérdida.

## 🔧 Dependencias:

- `yfinance`: Para obtener los precios actuales de las acciones.
- `pandas`: Para manipulación de datos.
- `numpy`: Para operaciones numéricas.
- `matplotlib`: Para visualización de gráficos.
- `streamlit`: Para crear el dashboard interactivo.
- `curl_cffi`: Para manejo de errores HTTP.
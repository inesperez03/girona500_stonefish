# girona500_stonefish

Simulación del Girona500 UJI con manipulador Bravo en la piscina CIRTESU, siguiendo la estructura de `bluerov_stonefish`. El fichero `scenarios/girona500_uji_bravo.scn` usa los recursos incluidos en este paquete y adapta los propulsores a Stonefish 1.6.

## Recursos del modelo

Las mallas y texturas que usa el escenario local están en `data/girona500` y `data/bravo7`. El paquete `girona500_description` aporta el URDF y los marcos ROS 2; el lanzador lo inicia automáticamente. Proceden de:

- Girona500: https://github.com/srv/girona500_description, revisión `6ec4cdc1bf30b692fb47785d105e7f50b741a8ee`.
- Bravo 7: https://github.com/slopezba/blueprintlab_reachbravo7_manipulator_description, revisión `84b1b0852192ba777ff81e0cc63c700ad7f72b60`.

Se copiaron únicamente los 51 archivos referenciados por el escenario. Los repositorios de origen no publican una licencia de redistribución clara; conviene verificarla antes de distribuir el paquete.

## Uso

Clona este repositorio en el directorio `src` de un workspace ROS 2 Humble. Necesitas `stonefish_ros2` y `girona500_description` en el mismo workspace o instalados en el entorno ROS.

```bash
colcon build --packages-select girona500_stonefish
source install/setup.bash
ros2 launch girona500_stonefish girona500_cirtesu.launch.py
```

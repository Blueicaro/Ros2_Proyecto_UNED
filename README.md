# Ros2_Proyecto_UNED

Este repositorio contiene mi proyecto para el curso de introducción a ROS impartido por la [UNED](https://www.uned.es/universidad/inicio), en el año 2026.


## Ejercicio 1

Se pide implementar un sistema de tres nodos (A,B,C). Los nodos A y B deben comunicarse en un servicio. Siendo A el cliente y B el servidor. Los nodos A y C deben comunicarse mediante una acción. Esta acción se ejecutará en C de forma que que debe comunicarse 5 veces mediante un servicio en el nodo B. Tras cada comunicación, debe realimentar al nodo A con el número de iteraciones que le quedan hasta concluir la comunicación.

Para la realizacion de este ejercicio se creó el paquete my_interfaces, dónde se definen dos interfaces.

Se crea un lanzador para probar los nodos todos juntos: 

´´´
      
        ros2 launch my_launch ejercicio1.launch.xml 

´´´

## Ejercicio 2

Paquete: ejercicio_py_2

1. Hacer un nodo que publique la transformada de 3 ejes, y visualizarla en rviz2:

                * Base_Link -> Sensor1_Link

                * Base_Link -> Sensor2_Link

                * Base_Link -> Sensor3_Link
        
Para resolver este punto se crea el nodo publish_tf. Se lanza con el siguiente comando:

        ´´´
        ros2 run ejercicio_py_2 publish_tf_node 
        ´´´        



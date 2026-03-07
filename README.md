# Ros2_Proyecto_UNED

Este repositorio contiene mi proyecto para el curso de introducción a ROS impartido por la [UNED](https://www.uned.es/universidad/inicio), en el año 2026.

# Contenido


- [Ros2\_Proyecto\_UNED](#ros2_proyecto_uned)
- [Contenido](#contenido)
  - [Ejercicio 1](#ejercicio-1)
  - [Ejercicio 2](#ejercicio-2)
  - [Ejercicio 3](#ejercicio-3)



## Ejercicio 1

Se pide implementar un sistema de tres nodos (A,B,C). Los nodos A y B deben comunicarse en un servicio. Siendo A el cliente y B el servidor. Los nodos A y C deben comunicarse mediante una acción. Esta acción se ejecutará en C de forma que que debe comunicarse 5 veces mediante un servicio en el nodo B. Tras cada comunicación, debe realimentar al nodo A con el número de iteraciones que le quedan hasta concluir la comunicación.

Para la realizacion de este ejercicio se creó el paquete my_interfaces, dónde se definen dos interfaces.

Se crea un lanzador para probar los nodos todos juntos: 

´´´
      
        ros2 launch my_launch ejercicio1.launch.xml 

´´´

## Ejercicio 2

Paquete: ejercicio_py_2

1. Crear un nodo que publique tres TFs estáticos: base_link → sensor_1, base_link → sensor_2, base_link → sensor_3 y visualizar en RViz.

                * Base_Link -> Sensor1_Link

                * Base_Link -> Sensor2_Link

                * Base_Link -> Sensor3_Link
        
Para resolver este punto se crea el nodo publish_tf. Se lanza con el siguiente comando:

        ´´´
        ros2 run ejercicio_py_2 publish_tf_node 

2. Modificar el nodo dinámico de ejemplo para que un frame se mueva en un patrón 8 (figura de “8”) alrededor de base_link.

Se crea un nodo nuevo llamado publish_tf_node2, que es un copia del anterior y se añade un 
nuevo link llamado arm_link, el cual se mueve en forma de 8 con respecto a al nodo base_link

Se lanza con con el siguiente comando:

        ros2 run  ejercicio_py_2 publish_tf_node2

3. Combinar TFs estáticos y dinámicos: un sensor en movimiento relativo a un brazo que se mueve

Este paquete anterior ya hace esta funcionalidad


4. Escribir un nodo que consulte el TF de rotating_link respecto a base_link y publique la distancia al frame en un topic.

Se crea el nodo publish_distance, publica un topico llamado distancia.

Para pobrar este punto, ejecutar en un terminal el nodo del punto anterior:

                ros2 run  ejercicio_py_2 publish_tf_node2

Y en otro terminal ejecutar:

                ros2 run ejercicio_py_2 publish_distance 


Por último en otro terminar ejecutar:

                ros2 topic echo /distancia


## Ejercicio 3

Ejercicio práctico final — Construye tu primer robot completo 

Objetivo:
Diseñar un robot móvil diferencial sencillo en URDF/XACRO y visualizarlo correctamente en RVIZ2.

Se crea el paquete robot_ejercicio3. En este paquete se crea un directorio con el nombre URDF, donde se alojan los archivos siguientes:

        * robot_ejercio3.xacro. Este es el archivo principal que debe llamar
        * robot_common.xacro. Este archivo contiene definiciones de colores y macros de para el cálculo de las inercias
        * robot_geometry.xacro. Este archivo contiene la geometria del robot. La definición está parametrizada con variables

Para visualizar el robot en rviz2 ejecutar:

        ros2 launch urdf_tutorial display.launch.py model:=/home/<user>/curso_ros2_ws/src/Ros2_Proyecto_UNED/robot_ejercicio3/urdf/robot_ejercicio3.xacro 

Cuando esté funcionando se puede lanzarar el siguiente comando para generar un archivo PDF y comprobar que todas las relaciones de los links son correctas:

        ros2 run tf2_tools view_frames

                

                

       


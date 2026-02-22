# Ros2_Proyecto_UNED
Este repositorio contiene mi proyecto para el curso de ROS2 de la Uned

Primera copia

## Ejercicio 1

Se pide implementar un sistema de tres nodos (A,B,C). Los nodos A y B deben comunicarse en un servicio. Siendo A el cliente y B el servidor. Los nodos A y C deben comunicarse mediante una acción. Esta acción se ejecutará en C de forma que que debe comunicarse 5 veces mediante un servicio en el nodo B. Tras cada comunicación, debe realimentar al nodo A con el número de iteraciones que le quedan hasta concluir la comunicación.

Se crea un lanzador para probar los nodos todos juntos: 
        
        ros2 launch my_launch ejercicio1.launch.xml 
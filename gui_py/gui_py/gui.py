import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,QLabel
import sys


class RoombaNode(Node):
    def __init__(self):
        super().__init__('room')
        self.get_logger().info("Nodo room iniciado")
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
    
    def move_forward(self):
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        self.publisher_.publish(msg)
        self.get_logger().info("Publicando comando de movimiento hacia adelante")
        
    def stop(self):
        msg = Twist()
        msg.linear.x = 0.0  # Detener el movimiento
        self.publisher_.publish(msg)
        self.get_logger().info("Publicando comando de detención")
        
    def move_left(self):
        msg = Twist()
        msg.angular.z = 1.0  # Velocidad de giro hacia la izquierda
        self.publisher_.publish(msg)
        self.get_logger().info("Publicando comando de giro hacia la izquierda")
        
    def move_right(self):
        msg = Twist()
        msg.angular.z = -1.0  # Velocidad de giro hacia la derecha
        self.publisher_.publish(msg)
        self.get_logger().info("Publicando comando de giro hacia la derecha")
        
    def retroceder(self):
        msg = Twist()
        msg.linear.x = -2.0  # Velocidad hacia atrás
        self.publisher_.publish(msg)
        self.get_logger().info("Publicando comando de movimiento hacia atrás")


class MainWindow(QMainWindow):
    def __init__(self,ros_node):
        
        super().__init__()
        self.ros_node = ros_node
        
        self.setWindowTitle("Entorno Qt")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        
        layout = QVBoxLayout()
        
        buttonAvance = QPushButton("Avanzar")
        buttonAvance.clicked.connect(self.ros_node.move_forward)  # Conectar el botón de avance al método move_forward del nodo
        layout.addWidget(buttonAvance)
        
        buttonIzquierda = QPushButton("Girar Izquierda")
        buttonIzquierda.clicked.connect(self.ros_node.move_left)  # Conectar el botón de giro a la izquierda al método move_left del nodo
        layout.addWidget(buttonIzquierda)
        
        buttonDerecha = QPushButton("Girar Derecha")
        buttonDerecha.clicked.connect(self.ros_node.move_right)  # Conectar el botón de giro a la derecha al método move_right del nodo
        layout.addWidget(buttonDerecha)

        buttonRetroceder = QPushButton("Retroceder")
        buttonRetroceder.clicked.connect(self.ros_node.retroceder)  # Conectar el botón de retroceso al método retroceder del nodo
        layout.addWidget(buttonRetroceder)

        buttonStop = QPushButton("Detener")
        buttonStop.clicked.connect(self.ros_node.stop)  # Conectar el botón de detención al método stop del nodo
        layout.addWidget(buttonStop)
        
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.etiqueta = QLabel("¡Control roomna en Qt!")
        layout.addWidget(self.etiqueta)




def main():
    rclpy.init()
    node = RoombaNode()
    
    app = QApplication(sys.argv)
    window = MainWindow(node)
    window.show()
    # Timer de ROS2 en el hilo principal de Qt
    timer = node.create_timer(0.1, lambda: None)  # Timer para mantener el nodo activo y procesar eventos de ROS2   
    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.0   )  # Procesar eventos de ROS2 a máxima velocidad
            app.processEvents() # Procesar eventos de Qt
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()
   
        
if __name__ == "__main__":
    main()
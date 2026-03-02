import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
class publishtfnode(Node):
    def __init__(self):
        super().__init__("static_tf")
       

        # Definimos el perfil de salida
        qos_publisher = QoSProfile(depth=10,reliability=ReliabilityPolicy.BEST_EFFORT, durability=DurabilityPolicy.VOLATILE)
        self.angle = 0
        # Posición del link que gira
        self.centroX_ = 0.0
        self.centroY_ = 0.0
        self.centroZ_ = 0.5
        self.escala_= 0.4
        self.br_ = TransformBroadcaster(self,qos_publisher)
        self.timer_ = self.create_timer(1.0,self.broadcaster_tf)
        self.timerfast_ = self.create_timer(0.1,self.publish_dynamic_tf)
        
    def sensor1_broadcaster(self):
        
        # TF desde base a sensor 1
        tf = TransformStamped()
        tf.header.frame_id = "base_link"
        tf.child_frame_id = "sensor_1"
        tf.header.stamp = self.get_clock().now().to_msg()
        # Unidades en metros
        tf.transform.translation.x = 0.0
        tf.transform.translation.y = 0.2
        tf.transform.translation.z = 0.2
        tf.transform.rotation.x = 0.0
        tf.transform.rotation.y = 0.0
        tf.transform.rotation.z = 0.7071
        tf.transform.rotation.w = 0.7071
        self.br_.sendTransform(tf)
    
    def sensor2_broadcaster(self):
        #TF desde base a sensor 2
        tf = TransformStamped()
        tf.header.frame_id = "base_link"
        tf.child_frame_id = "sensor_2"
        tf.header.stamp = self.get_clock().now().to_msg()
         # Unidades en metros
        tf.transform.translation.x = 0.0
        tf.transform.translation.y = -0.2
        tf.transform.translation.z = 0.2
        tf.transform.rotation.x = 0.0
        tf.transform.rotation.y = 0.0
        tf.transform.rotation.z = -0.7071
        tf.transform.rotation.w = 0.7071
        self.br_.sendTransform(tf)
        
    def sensor3_broadcaster(self):
        #TF desde base a sensor 3
        tf = TransformStamped()
        tf.header.frame_id = "base_link"
        tf.child_frame_id = "sensor_3"
        tf.header.stamp = self.get_clock().now().to_msg()
        # Unidades en metros       
        
        tf.transform.translation.x = 0.2
        tf.transform.translation.y = 0.0
        tf.transform.translation.z = 0.0
        self.br_.sendTransform(tf)
        
    def publish_dynamic_tf(self):
    
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'base_link'
        t.child_frame_id = 'arm_link'

        # Brazo girando en yaw
        t.transform.translation.x = self.centroX_+(self.escala_*math.sin(self.angle))
        t.transform.translation.y = self.centroY_+(self.escala_*math.sin(self.angle)*math.cos(self.angle))
        t.transform.translation.z = self.centroZ_

       

        self.br_.sendTransform(t)
        self.angle += 0.05
        if self.angle > (2*math.pi):
            self.angle = 0
        

    def broadcaster_tf(self):
        
        self.sensor1_broadcaster()
        self.sensor2_broadcaster()
        self.sensor3_broadcaster()    
        
       
        
       


def main(args=None):
    rclpy.init(args=args)
    node = publishtfnode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
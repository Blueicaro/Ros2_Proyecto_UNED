import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

class publishtfnode(Node):
    def __init__(self):
        super().__init__("static_tf")
        self.br_ = TransformBroadcaster(self)
        self.timer_ = self.create_timer(1.0,self.broadcaster_tf)

    def broadcaster_tf(self):
        # TF desde base a sensor 1
        tf1 = TransformStamped()
        tf1.header.frame_id = "base_link"
        tf1.child_frame_id = "sensor_1"
        tf1.header.stamp = self.get_clock().now().to_msg()
        # Unidades en metros
        tf1.transform.translation.x = 0.0
        tf1.transform.translation.y = 0.2
        tf1.transform.translation.z = 0.2
        tf1.transform.rotation.x = 0.0
        tf1.transform.rotation.y = 0.0
        tf1.transform.rotation.z = 0.7071
        tf1.transform.rotation.w = 0.7071
        self.br_.sendTransform(tf1)

          #TF desde base a sensor 2
        tf2 = TransformStamped()
        tf2.header.frame_id = "base_link"
        tf2.child_frame_id = "sensor_2"
        tf2.header.stamp = self.get_clock().now().to_msg()
         # Unidades en metros
        tf2.transform.translation.x = 0.0
        tf2.transform.translation.y = -0.2
        tf2.transform.translation.z = 0.2
        tf2.transform.rotation.x = 0.0
        tf2.transform.rotation.y = 0.0
        tf2.transform.rotation.z = -0.7071
        tf2.transform.rotation.w = 0.7071
        self.br_.sendTransform(tf2)

        #TF desde base a sensor 2
        tf3 = TransformStamped()
        tf3.header.frame_id = "base_link"
        tf3.child_frame_id = "sensor_3"
        # Unidades en metros
        tf3.transform.translation.x = 0.2
        tf3.transform.translation.y = 0.0
        tf3.transform.translation.z = 0.2
        self.br_.sendTransform(tf3)


def main(args=None):
    rclpy.init(args=args)
    node = publishtfnode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
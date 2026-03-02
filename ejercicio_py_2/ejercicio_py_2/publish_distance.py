import rclpy
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy
import numpy as np
from rclpy.node import Node
from tf2_msgs.msg import TFMessage
from std_msgs.msg import Float64



class PublishDistanceNode(Node):
    def __init__(self):
        super().__init__("Publish_Distance")
        
        qos_profile = QoSProfile(depth=10,reliability=ReliabilityPolicy.BEST_EFFORT, durability=DurabilityPolicy.VOLATILE)
        
        self.subcrip_ = self.create_subscription(TFMessage,"/tf",self.transform_callback,qos_profile)   
        self.publish_ = self.create_publisher (Float64,"distancia",10)
        self.get_logger().info("PublishDistanceNode running")
        
    def transform_callback(self, msg:TFMessage):
       for t in msg.transforms:
           hijo = t.child_frame_id
           if hijo =="arm_link":
               dist_x = t.transform.translation.x
               dist_y = t.transform.translation.y
               dist_z = t.transform.translation.z
               distancia = np.linalg.norm([dist_x,dist_y,dist_z])
               self.get_logger().info(f"Distancia a arm_link: {distancia:.2f} metros")
               msg_publish = Float64()
               msg_publish.data = distancia
               self.publish_.publish(msg_publish)
               break 
            

def main(args=None):
    rclpy.init(args=args)
    node = PublishDistanceNode()
    rclpy.spin(node)
    rclpy.shutdown
    
    
if __name__=="__main__":
    main()
            
            
            
   
    

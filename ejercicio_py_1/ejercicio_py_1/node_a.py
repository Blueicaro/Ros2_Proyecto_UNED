import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle, GoalStatus
from my_interfaces.srv import IntHex
from my_interfaces.action import Aleatorio

class IntHexClientNode(Node):
    def __init__(self):
        super().__init__("IntHex_Client")
        self.cliente_ = self.create_client(IntHex,"convert_hex")
        self.random_convert_ = ActionClient(self,Aleatorio,"acc_server")
        self.get_logger().info("IntHexClientNode running")
        
    def call_convert_int(self,valor):
        # Esperar por el servidor
        self.get_logger().info("IntHexClientNode call_convert_int")
        while not self.cliente_.wait_for_service(1.0):
            self.get_logger().warn("Esperando por el servidor")
        
        # Petición que enviamos al servidor
        request = IntHex.Request()
        request.valor = valor
        future = self.cliente_.call_async(request)
        future.add_done_callback(self.callback_conversion_done)
        
    def callback_conversion_done(self,future):
        # respuesta que recibimos del servidor
        response = future.result()
        self.get_logger().info("Conversión ok: "+str(response.exito))
        self.get_logger().info("Valor en hexadecimal: "+response.sthex)
        
    def send_goal(self):       
        self.random_convert_.wait_for_server()
        goal = Aleatorio.Goal()
        goal.run = True
        self.random_convert_.send_goal_async(goal,feedback_callback=self.goal_feedback_callback).add_done_callback(self.goal_response_callback)
      
      
    def goal_feedback_callback(self,feedback_msg):
        valor = feedback_msg.feedback.current        
        self.get_logger().info("FeedBack: "+str(valor))
        
    def goal_response_callback(self,future):
        goal_handle :ClientGoalHandle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rechazado")
            return
        goal_handle.get_result_async().add_done_callback(self.goal_result_callback)        
        
    def goal_result_callback(self,future):
        status = future.result().status
        result = future.result().result
        
        if status ==GoalStatus.STATUS_ACCEPTED:
            self.get_logger().info("Exito")
        self.get_logger().info("goal_result_callback: "+result.valor)
        
def main(args=None):
    rclpy.init(args=args)
    node = IntHexClientNode()
   # node.call_convert_int(255)
    node.send_goal()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__=="__main__":
    main()
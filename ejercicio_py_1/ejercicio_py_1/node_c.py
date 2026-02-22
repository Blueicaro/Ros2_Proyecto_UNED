import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer,GoalResponse
from rclpy.action.server import ServerGoalHandle
from my_interfaces.srv import IntHex
from my_interfaces.action import Aleatorio

import random


class ActionServerNode(Node):
   
    
    def __init__(self):
        super().__init__("Accion_Server")
        self.cliente_ = self.create_client (IntHex,"convert_hex")
        self.action = ActionServer(
                    self,
                    Aleatorio,
                    "acc_server",
                    goal_callback=self.goal_callback,
                    execute_callback=self.execute_callback)
        self.get_logger().info("Action Server arrancado")
        
    
    def goal_callback(self, goal_request: Aleatorio.Goal):
        # Procesar callback
        self.get_logger().info("Goal recibido")
        if goal_request.run == False:
            self.get_logger().warn("Goal rechazado")
            return GoalResponse.REJECT
        self.get_logger().info("Goal aceptado")
        return GoalResponse.ACCEPT
            
            
    
    async def execute_callback(self,goal_handle:ServerGoalHandle):
        while not self.cliente_.wait_for_service(1.0):
            self.get_logger().info("Action Server esperando al servidor")
            
                
        request = IntHex.Request()
        resultado = Aleatorio.Result()
        feedback = Aleatorio.Feedback()
    
        for i in range(5):
            request.valor = random.randint(1,100)
            future = self.cliente_.call_async(request)
            future.add_done_callback(self.callback_conversion_done) 
            respuesta = await future    
            feedback.current = i
            goal_handle.publish_feedback(feedback)
  
        
        if respuesta.exito:
            goal_handle.succeed()
            resultado.valor = respuesta.sthex
        else:
            goal_handle.abort()
            resultado.valor=""
            
        return resultado
        
        
        
    
    def callback_conversion_done(self,future):
        respuesta = future.result()       
        self.get_logger().info("Conversión ok: "+str(respuesta.exito))
        self.get_logger().info("Valor en hexadecimal: "+respuesta.sthex)
       
    
    

        
    
def main(args=None):
    rclpy.init(args=args)
    node = ActionServerNode()   
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__=="__main__":
    main()
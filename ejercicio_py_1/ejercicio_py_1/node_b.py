import rclpy
from rclpy.node import Node
from my_interfaces.srv import IntHex


class IntToHexServerNode(Node):
    def __init__(self):
        super().__init__("IntToHex_Server")
        self.converttohex = self.create_service(IntHex,"convert_hex",self.callback_convert_hex)
        self.get_logger().info("ntToHexServerNode running")
        
    def callback_convert_hex(self, request: IntHex.Request, reponse: IntHex.Response):
        if request.valor < 0:
            reponse.exito = False
            reponse.sthex="";
        else:
            reponse.exito = True
            reponse.sthex = hex(request.valor)
        return reponse
    
def main(args=None):
    rclpy.init(args=args)
    node = IntToHexServerNode()
    rclpy.spin(node)
    rclpy.shutdown
    
if __name__ =="__main__":
    main()
        
        
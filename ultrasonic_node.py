import serial
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class UltrasonicNode(Node):
    def __init__(self):
        super().__init__('ultrasonic_node')
        self.publisher1_ = self.create_publisher(Int32, 'ultrasonic_distance', 10)
        self.publisher2_ = self.create_publisher(Int32, 'ultrasonic_distance2', 10)
        self.serial = serial.Serial('/dev/ttyACM0', 115200)  # 포트 및 속도 설정

        self.timer = self.create_timer(0.1, self.publish_distance)

    def publish_distance(self):
        try:
            data = self.serial.readline().decode().strip()
            #print(f"Recevived data: {data}")

            splitted_data = data.split(',')
            #print(f"Splitted data: {splitted_data}")
            
            distance1, distance2 = map(int, splitted_data)  # 데이터 분리 및 변환
            
            distance_msg1 = Int32()
            distance_msg1.data = distance1
            
            distance_msg2 = Int32()
            distance_msg2.data = distance2
            
            self.publisher1_.publish(distance_msg1)
            self.publisher2_.publish(distance_msg2)
           
            
        #except UnicodeDecodeError:
        except (UnicodeDecodeError, ValueError):
            pass

def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    

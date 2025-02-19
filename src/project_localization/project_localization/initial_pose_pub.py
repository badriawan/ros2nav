# initial_pose_pub.py

import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PointStamped


class InitialPosePublisher(Node):

    def __init__(self):
        super().__init__('initial_pose_publisher')
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, '/initial_pose', 1)
        self.subscription = self.create_subscription(
            PointStamped,
            '/clicked_point',
            self.callback,
            1)

    def callback(self, msg):
        initial_pose_msg = PoseWithCovarianceStamped()
        initial_pose_msg.x = msg.point.x
        initial_pose_msg.y = msg.point.y
        self.publisher_.publish(initial_pose_msg)
        self.get_logger().info('Published initial pose: x=%f, y=%f' % (initial_pose_msg.x, initial_pose_msg.y))

def main(args=None):
    rclpy.init(args=args)
    initial_pose_publisher = InitialPosePublisher()
    rclpy.spin(initial_pose_publisher)
    initial_pose_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


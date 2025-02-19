import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
from nav2_msgs.action import NavigateToPose

class NavToPoseActionClient(Node):

    def __init__(self):
        super().__init__('nav_to_pose_action_client')
        self.action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

        self.subscription = self.create_subscription(
            PointStamped,
            '/clicked_point',
            self.clicked_point_callback,
            10)

    def clicked_point_callback(self,msg):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.pose.position = msg
        goal_msg.pose.pose.orientation.w = 1.0

        self.send_goal(goal_msg)

    def send_goal(self, goal_msg):
        self.action_client.wait_for_server()
        self.action_client.send_goal_async(goal_msg)

def main(args=None):
    rclpy.init(args=args)

    nav_to_pose_action_client = NavToPoseActionClient()

    rclpy.spin(nav_to_pose_action_client)

    nav_to_pose_action_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
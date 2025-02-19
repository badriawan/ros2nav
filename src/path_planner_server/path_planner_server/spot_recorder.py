#!/usr/bin/env python

import rclpy
from geometry_msgs.msg import PointStamped
from std_srvs.srv import Trigger, TriggerResponse
from custom_interfaces.srv import save_spot


class SpotRecorder:
    def __init__(self):
        self.node = rclpy.create_node('spot_recorder')
        self.spots = {}  # Dictionary to store spot labels and coordinates
        self.save_service = self.node.create_service(Trigger, '/save_spot', self.handle_save_spot)
        self.end_string = "end"
    
    def handle_save_spot(self, request, response):
        if request.data == self.end_string:
            self.save_spots_to_file()
            response.success = True
            response.message = "File saved successfully"
        else:
            self.spots[request.data] = self.get_current_coordinates()
            response.success = True
            response.message = "Spot saved: {}".format(request.data)
        return response
    
    def get_current_coordinates(self):
        # Function to get current position and orientation of the robot
        # This is just a placeholder, you should replace this with actual code to get the coordinates
        current_pose = PointStamped()
        return current_pose
    
    def save_spots_to_file(self):
        with open('spots.txt', 'w') as file:
            for label, coordinates in self.spots.items():
                file.write("{}: {}\n".format(label, coordinates))
    
    def run(self):
        rclpy.spin(self.node)

def main(args=None):
    rclpy.init(args=args)
    spot_recorder = SpotRecorder()
    spot_recorder.run()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

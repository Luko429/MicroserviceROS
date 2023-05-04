import time

ROSPipe = 'ROSPipe.txt'


def writeToFile(file, message):
    while True:
        try:
            with open(file, 'w') as openPipe:
                openPipe.write(message)
            break
        except:
            time.sleep(1)


text = '''
target_term = ["service"]

terms_and_definitions = {
    "service" = "A service is another form of communication between nodes in ROS, using a request-response pattern."
    "node" = "A node is a basic unit of computation in the ROS system, representing a single running process."
    "ros" = "ROS is short for Robot Operating Systems. It is not an actual operating system, 
    but a set of tools that provide functionality of a robot."
    "request-response pattern" = "Definition for request-response pattern"
}
'''

input('Press Enter to write the text to the ROSPipe.txt?')

writeToFile(ROSPipe, text)
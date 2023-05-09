# MicroserviceROS
CS361 Microservice for my partner's ROS project

# Instructions on how to REQUEST data from the microserviceROS.py: 
# 1. You must have a file called ROSPipe.txt in the same directory that you start the microserviceROS.py
# 2. In the message you want to send, you must have the strings 'target_term' and 'terms_and_definitions'
# within the message.  
# a. The message must have an equal sign following the 'target_term' 
# b. The message must have the target term surrounded in double quotes that is surrounded in brackets. 
# 3. The message must have an equals sign following the 'terms_and_definitions' 
# a. The message must have a curly brackets following this equal sign that has each term in double 
# quotes followed by an equal sign and its corresponding definition in double quotes.  

# Instructions on how to RECEIVE data from the microserviceROS.py
# 1. After a successful request the microserviceROS.py will find the definition of the target term
# within the terms_and_definitions array.  
# 2. It will then find and return a set of any terms that appear within the target's definition
# that are also terms within the terms_and_definitions array.  
# a. Note that the terms within the definition must match the syntax of the terms in the terms_and_
# definitions array except for case.  
# 3. The microserviceROS.py will return a string in the ROSPipe.txt file with related_terms followed
# by an equal sign and a string array of each term.  
# 4. In order to RECEIVE this data the ROSPipe.txt file must be read and the string that is read must be checked for 
# the 'related_terms' string.  Then the following array can be parsed for each string within the array.  
# Here is an example of the REQUEST:
`
target_term = ["service"]

terms_and_definitions = {
    "service" = "A service is another form of communication between nodes in ROS, using a request-response pattern."
    "node" = "A node is a basic unit of computation in the ROS system, representing a single running process."
    "ros" = "ROS is short for Robot Operating Systems. It is not an actual operating system, 
    but a set of tools that provide functionality of a robot."
    "request-response pattern" = "Definition for request-response pattern"
}
`
# Here is an example of the RESPONSE to the REQUEST
`
related_terms = ['request-response pattern', 'node', 'ros']
`
# Here is the UML sequence diagram for the ROS microservice system:
![UML](https://user-images.githubusercontent.com/98900778/236966550-bcb74cb5-5d49-4c2e-ba7f-4bef8220f847.JPG)

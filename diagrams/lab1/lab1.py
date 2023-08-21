from diagrams import Cluster, Diagram
from diagrams.oci.devops import APIGateway
from diagrams.generic.os import IOS, Android, Windows, LinuxGeneral
from diagrams.generic.device import Mobile, Tablet
from diagrams.programming.language import Go, Nodejs, Java, Python
  
# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("Lab #1", show=True, outformat="jpg"):
    # definice uzlu
 
    apigw = APIGateway("API Gateway")
 
    clients = [Mobile("Mobile"),
               Tablet("Mobile"),
               Windows("Desktop"),
               LinuxGeneral("Desktop"),
               IOS("Desktop")
               ]

    with Cluster("Backends"):
        backends = [Go("Microservice"),
                    Nodejs("Microservice"),
                    Java("Microservice"),
                    Python("Microservice")
                    ]

 
    # propojeni uzlu grafu orientovanymi hranami
    clients >> apigw >> backends
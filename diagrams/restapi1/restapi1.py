from diagrams import Cluster, Diagram
from diagrams.oci.devops import APIGateway
from diagrams.generic.os import IOS, Android, Windows, LinuxGeneral
from diagrams.generic.device import Mobile, Tablet
from diagrams.programming.language import Go, Nodejs, Java, Python
  
# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("Rest API dnes", show=True, direction="TB", outformat="jpg"):
    # definice uzlu

    with Cluster("Retails frontends"):
        fe1 = Mobile("Mobile FE")
        fe2 = Tablet("Mobile FE")
        fe3 = LinuxGeneral("Destop FE")
        fe4 = IOS("Destop FE")

    with Cluster("3rd party supplier"):
        supplier = [Go("Microservice"),
                Go("Microservice")]

    with Cluster("3rd party customer"):
        customer = [Python("Microservice"),
                Python("Microservice")]

    with Cluster("Company"):
        with Cluster("k8s"):
            bes1 = [Go("Microservice"),
                        Go("Microservice"),
                        Java("Microservice"),
                        Java("Microservice")
                        ]
        
        be2 = Java("Microservice")
        be3 = Java("Microservice")
        be4 = Java("Microservice")




 
    # propojeni uzlu grafu orientovanymi hranami
    fe1 >> bes1[0]
    fe1 >> bes1[1]
    fe2 >> bes1[0]
    fe2 >> bes1[1]
    fe3 >> bes1[2]
    fe3 >> bes1[3]
    fe4 >> bes1[2]
    fe4 >> bes1[3]
    supplier >> be2
    supplier >> bes1[0]
    customer >> be3
    customer >> be4
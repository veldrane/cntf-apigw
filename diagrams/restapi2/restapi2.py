from diagrams import Cluster, Diagram
from diagrams.oci.devops import APIGateway
from diagrams.generic.os import IOS, Android, Windows, LinuxGeneral
from diagrams.generic.device import Mobile, Tablet
from diagrams.programming.language import Go, Nodejs, Java, Python
  
# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("Api Gateway", show=True, direction="TB", outformat="jpg"):
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



        apigw1 = APIGateway("API Gateway")
        apigw2 = APIGateway("API Gateway")
 
    # propojeni uzlu grafu orientovanymi hranami
    fe1 >> apigw1
    fe2 >> apigw1
    fe3 >> apigw1
    fe4 >> apigw1
    supplier >> apigw1
    apigw1 >> bes1
    apigw1 >> be2
    customer >> apigw2
    apigw2 >> be3
    apigw2 >> be4

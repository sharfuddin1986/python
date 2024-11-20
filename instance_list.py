ec2_instance_info = [
    {
        "id": "instance001",
        "type": "t2.micro",
        "service": "Application_server_1"
    },    
    {   
         "id": "instance002",
        "type": "t2.medium",
        "service": "web_server_1"

    },
    { 
        "id": "instance003",
        "type": "t2.large",
        "service": "Application_server_2"
    },
    {
        "id": "instance004",
        "type": "t2.medium",
        "service": "web_server_2"

    }

]
print(ec2_instance_info[0]["type"])

### To run this application you need two repo
| This is simple Demo Application as Microservices between 2 server.
1. webServer: which is running Flask-Server and also sending some traces to the grpcServer
2. grpcServer: It is accepting data like

```text
Message Received: page_name: "http://127.0.0.1:5000/"      
client_address: "127.0.0.1:5000"                           
request_body: "{}"                                         
, content: <grpc._server._Context object at 0x7f9beb477290>
```
---
Now, Let's discuss how we can start it.
1. clone the repos
2. build docker with following command
```bash
$ docker build -t flaskserver:latest .
$ docker build -it grpcserver:latest .
```
3. before running the docker image, create a network
```bash
$ docker network create idocnet
```
4. now, run the images in the network
```bash
$ docker run --rm -it --network idocnet --name flaskserver -p 5000:5000 flaskserver
$ docker run --rm -it --network idocnet --name grpcserer grpcserer
```
5. now, inspect the network and take a look if all services are attached to network or not.
```bash
$  docker network inspect idocnet
```
```text
[                                                                                
    {                                                                            
        "Name": "idocnet",                                                       
        "Id": "fff1e17551e5c315e1772141dba01e7e979714356e871bd43233af96f90d3256",
        "Created": "2023-09-28T17:42:02.731392123Z",                             
        "Scope": "local",                                                        
        "Driver": "bridge",                                                      
        "EnableIPv6": false,                                                     
        "IPAM": {                                                                
            "Driver": "default",                                                 
            "Options": {},                                                       
            "Config": [                                                          
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "14079458ae315679da810aed7332e9918e9d52470b46b1be24d020755d5ba54d": {
                "Name": "grpcserver",
                "EndpointID": "23e69e42f8a1195df1a129c4f1eff2bc1da11643e0bd4a9fc08c0ba73d1eaf52",
                "MacAddress": "02:42:ac:12:00:03",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            },
            "b80ad8039194321acafb089ee7a74e78ea86455df7271bf021ea6f0656b578be": {
                "Name": "flaskserver",
                "EndpointID": "f97f33183a5191d07165e3f060f33b00cbd9fbcc360b64d770163e6b152a21e6",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]

```
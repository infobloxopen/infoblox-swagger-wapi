# <img src="https://info.infoblox.com/rs/240-PTK-751/images/InfoBloxLogo.png" width="300">


-----------
                            	      Copyright 2020                                            
                      	Author: Vedant Sethia <vsethia@infoblox.com>                         
  		For any issues/suggestions please write to vsethia@infoblox.com , kvasudevan@infoblox.com           

-----------

# WAPI Documentation using Swagger  


## Swagger 
Swagger is an open-source software framework backed by a large ecosystem of tools that helps developers design, build, document, and consume RESTful web services. While most users identify Swagger by the Swagger UI tool, the Swagger toolset includes support for automated documentation, code generation, and test-case generation. Sponsored by SmartBear Software, Swagger has been a strong supporter of open-source software, and has widespread adoption.

* [swagger-ui-dist](https://www.npmjs.com/package/swagger-ui-dist) is a dependency-free module that includes everything you need to serve Swagger UI in a server-side project, or a single-page application that can't resolve npm module dependencies.

## Open-API Specification
The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to RESTful APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection. When properly defined, a consumer can understand and interact with the remote service with a minimal amount of implementation logic.

An OpenAPI definition can then be used by documentation generation tools to display the API, code generation tools to generate servers and clients in various programming languages, testing tools, and many other use cases.

## Infoblox RESTful APIs
The Infoblox WAPI is an interface based on REST (REpresentational State Transfer). It uses HTTP methods and supports the primary or most-commonly-used HTTP verbs: POST, GET, PUT, and DELETE. These correspond to create, read, update, and delete (or CRUD) operations, respectively. It supports input and output in JSON and XML. All API calls are encrypted using SSL/TLS and authenticated using HTTP basic authentication.  These do not depend on any programming language. 

## Documentation
#### Pre-requisites
- Host machine with python 3.0+ and PHP 4.0+ (only for direct installation)
- CORS Plugin
- Connectivity between Grid master and Host

#### Installation
##### Direct Installation
- [Setup] Download the Infoblox-Swagger-WAPI repository and host it on a server (localhost/domain).
- [Access] Access this Swagger definition by http://<Host IP-Address/domain>/infoblox-swagger-ui/dist/home.php  

##### Docker
You can pull a pre-built docker image of the Infoblox-Swagger-UI directly from Docker Hub:

    docker pull vsethia/infoblox-wapi-swagger:v2
    docker run -p <PORT NO>:80 vsethia/infoblox-wapi-swagger:v2

This will start apache with Swagger UI on the specified PORT NO.

You can also create your own image using the Dockerfile given.

    docker build Dockerfile -t <username>/<project-name>:<version>
or

    docker build . -t <username>/<project-name>:<version>


## Instructions
After accessing "home.php":
- Enter the Grid Master IP-Address/FQDN and corresponding credentials on the homepage.
- Select the WAPI version.
- Click on the button to view the Swagger-UI





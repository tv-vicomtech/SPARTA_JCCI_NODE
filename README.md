## SPARTA JCCI NODE (or REST API )

This rest API is used to dynamically update the information in the SPARTA JCCI webpage, i.e NEXUS. 
Each partner should install this rest-API in order to manage their own information without problem, so for example they can change it without the permission of a central unit. The static content will remain in the main page, nevertheless, for the aim of the project it is strongly recommended to install this rest-API. The rest API is developed in a docker container in order to increase its usability and facilitate the deploy. 
All the partners information are stored in the folder 'data'.

## REQUIREMENTS

1) Install Docker - https://docs.docker.com/engine/install/

2) Download this repository

```git clone https://github.com/tv-vicomtech/SPARTA_JCCI_NODE.git```

3) The web service must be deployed in a machine with access to the internet and that can also be accessed and reached through a URL (domain or fix IP address + port + route).

> For example, get a public domain (for example, with [no-ip](https://www.noip.com/) ) for the HTTPS certificates in Keyrock, as well as configuring a DNS server if necessary.

4) It is also required to use TLS (HTTPS) certificates with a domain to secure communications.

> For example, generate certificates with [Let's Encrypt](https://letsencrypt.org/). It is necessary to have ports 80 and 443 free so that the [certbot](https://medium.com/@pentacent/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71) of Let's Encrypt is able to carry out the handshake to assure domain is owned by the machine.

## CHANGE DATA WITH YOUR INFORMATION

5) Go inside the folder data and update the files with your information

#### 5.1 Workbench
```cd SPARTA_JCCI_NODE/data``` # here there are all the information related with the Workbench section

NB. There are five files to be modified, each one follow a json structure. If your company not provide a data/interacion/tool/service, please remove the default information from the appropiate file and keep an empty structure in there.

```* description.jon = this file is a .json file that contains a general description of the activities and main goals of the partner```

```* data.jon = this file is a .json file that contains information about the used dataset used by the partner, where is possible find them, their versions, and a little description.```

```* interaction.jon = this file is a .json file that contains information about the available interactive services (for example Labs access, simulator access, etc) created by the partner, how is possible access to them, their versions, the contact detail, and a little description.```

```* services.jon = this file is a .json file that contains information about the available services created by the partner, how is possible access to them, their versions, the contact detail, and a little description.```

```* tools.jon = this file is a .json file that contains information about the available tools created by the partner, how is possible access to them, their versions, the contact detail, and a little description.```

All date fields using this format: dd/mm/YYYY

#### 5.2 Learning

Then, for update the information regarding your learning section go to the folder

```cd ../learning ```  or directly ```cd SPARTA_JCCI_NODE/learning ``` 

and please modify the 4 files with your information:

```* learning_data.json```
```* learning_interaction.json```
```* learning_services.json```
```* learning_tools.json```

All date fields using this format: dd/mm/YYYY

#### 5.3 Configuration WADL

Then, you should update one line in the WADL configuration file, so:

```cd ../wadl/ ```  or directly ```cd SPARTA_JCCI_NODE/wadl ``` 

and please modify the wadl_capabilities.xml file. In particular, the file define the path of the resource base (i.e. rest-api/node) so you have to update it according to your deployment as well as setting you PARTNER name.

Example (default config.)

```<resources base="10.200.5.38:5004/" name="VICOMTECH">```

New configuration

```<resources base="X.X.X.X:YYYY/" name="PARTNERNAME">```

 where X.X.X.X:YYYY are the ip and port where the rest-api (node) is deployed (NOTE, the default port is 5004)

#### 5.4 Empty Learning or Workbench content

Please, if you do not provide a specific learning content (data/services/tools/interaction) or a workbench content (data/services/tools/interaction) not remove its related file from the folder, just change its content with empty values, as shown in the example below:

Ex. * learning_tools.json

```
{
	"organization": "",
	"updated_date": "",
	"data":[	]
}
```


## CONFIGURE PROXY

6) Update the HTTPS certificates directory in docker-compose.yml file --> certs

7) Check that certificate filename are the same as the ones in the Dockerfile

8) [FOR THE FOLLOWING STEPS PLEASE CONTACT THE KEYROCK IDENTITY MANAGER ADMINISTRATOR IN THIS EMAIL ADDRESS: jafernandez@vicomtech.org, fzola@vicomtech.org] Generate PEP Proxy credentials to connect to Keyrock:

- Create Keyrock account in https://jcci.sparta.eu:4443 (if not enabled, ask for enabling to Keyrock administrator) and login.
- Register an application: https://fiware-idm.readthedocs.io/en/latest/user_and_programmers_guide/application_guide/index.html#register-an-application
- Register the proxy in the application just created: https://fiware-idm.readthedocs.io/en/latest/user_and_programmers_guide/application_guide/index.html#register-pep-proxy-and-iot-agents
- Asking to Keyrock administrator to enable the account

9) Update .env file:

- SPARTA_HOST -- domain of resource to be protected by proxy
- SPARTA_PORT -- port of resource to be protected by proxy

- SPARTA_PROXY_PORT -- port where proxy listens (http - unused protocol)
- SPARTA_PROXY_HTTPS_PORT -- port where proxy listens (https - the one to use)

- PEP_PROXY_APP_ID -- generated credentials by keyrock
- PEP_PROXY_USERNAME -- generated credentials by keyrock
- PEP_PASSWORD -- generated credentials by keyrock

## DEPLOY THE CONTAINER
10) Go in the main folder (SPARTA_JCCI_NODE) and build docker container

```cd ..```

```docker-compose up --build```
 
 ## ENABLE A PUBLIC ACCESS
11) Please provide to the JCCI Nexus manager (or the Task Leader) the information about the public IP:PORT where the rest-API can be consumed.
 

## SPARTA JCCI REST API 

This rest API is used to dynamically update the information in the SPARTA JCCI webpage, i.e NEXUS. 
Each partner should install this rest-API in order to manage their own information without problem, so for example they can change it without the permission of a central unit. The static content will remain in the main page, nevertheless, for the aim of the project it is strongly recommended to install this rest-API. The rest API is developed in a docker container in order to increase its usability and facilitate the deploy. 
All the partners information are stored in the folder 'data'.

## REQUIRIMENT

1) Install Docker - https://docs.docker.com/engine/install/

2) Download this repository

```git clone https://gitlab.vicomtech.es/SPARTA_EU3270_2018/jcci_sparta_api.git```

## CHANGE DATA WITH YOUR INFORMATION

3) Go inside the folder data and update the files with your information

```cd jcci_sparta_api/data```

```* description.jon = this file is a .json file that contains a general description of the activities and main goals of the partner```

```* data.jon = this file is a .json file that contains information about the used dataset used by the partner, where is possible find them, their versions, and a little description.```

```* interaction.jon = this file is a .json file that contains information about the available interactive services (for example Labs access, simulator access, etc) created by the partner, how is possible access to them, their versions, the contact detail, and a little description.```

```* services.jon = this file is a .json file that contains information about the available services created by the partner, how is possible access to them, their versions, the contact detail, and a little description.```

```* tools.jon = this file is a .json file that contains information about the available tools created by the partner, how is possible access to them, their versions, the contact detail, and a little description.```

## DEPLOY THE CONTAINER
4) Go in the main folder (jcci_sparta_api) and build docker container

```cd ..```

```docker build -t jcci_sparta_api .```

5) Run the container

 ```docker run -d -p 5004:5004 --name jcci_sparta_api jcci_sparta_api ```
 
 ## ENABLE A PUBLIC ACCESS
 6) Communicate to the Nexus responsabable (or the Task Leader) the information about the public IP:PORT where the rest-API can be consumed.

6) Please provide to the JCCI Nexus manager the public IP where you have publish the API service

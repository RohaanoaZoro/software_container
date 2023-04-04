Github URL: https://github.com/RohaanoaZoro/software_container

# software_container
Code for Front-End
All yaml files for kubernetes


#Run Commands

Flask
-python app.py

Angular
-npm i
-npm start 
-or npm run build

Mongo in Kubernertes
- kubectl apply -k . (in the mongodb folder)
#Note the path for the persistant volume should be changed accordingly

Deploy Applicatoin in kubernetes
helm install <name of application> <path_of_app> (This is located in ./Kubernetes/helm)

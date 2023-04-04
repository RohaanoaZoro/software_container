FROM node:latest as builder

#set the working dir 
WORKDIR /app

#Copy all files from current dir to node container
COPY . .

#Install all dependancies
RUN npm install && npm run ng build

#Run an Nginx container
FROM nginx:alpine

#Set the working dir
WORKDIR /usr/share/nginx/html

#Delete all old files in the working dir
RUN rm -rf ./*

#COPY ./myconfig.conf /etc/nginx/conf.d/

#Move the static build files to the nginx/html folder
COPY --from=builder /app/dist/angular-b2c-app .

#fast image build my_command
#COPY ./dist/angular-b2c-app/* .

#Create a folder to store all the images
#RUN mkdir assets

#RUN mv Beautiful_house_* ./assets/

#Start the application
ENTRYPOINT ["nginx", "-g", "daemon off;"]

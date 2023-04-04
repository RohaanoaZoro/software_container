openssl genrsa -des3 -out myecoprop.test.key 4096
openssl req -new -key myecoprop.test.key -out myecoprop.test.csr
cp myecoprop.test.key myecoprop.test.key.pw
openssl rsa -in myecoprop.test.key.pw -out myecoprop.test.key
openssl x509 -req -in myecoprop.test.csr -signkey myecoprop.test.key -out myecoprop.test.crt
sudo mkdir /etc/nginx/ssl
sudo cp myecoprop.test.crt /etc/nginx/ssl/
sudo cp myecoprop.test.key /etc/nginx/ssl/

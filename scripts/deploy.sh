#!/bin/bash

# Add Helm repo
helm repo add bitnami https://charts.bitnami.com/bitnami

# Create namespaces
# kubectl create ns db
# kubectl create ns web

# Fix path
cd ../

# Install MySQL
helm install mysql bitnami/mysql -n db -f cluster-config/mysql-values.yml

# Create API secret
kubectl apply -f cluster-config/web-secret.yml

# Build and load API image
sudo docker build -t api-image:latest api/
sudo docker save api-image:latest -o api-image.tar
sudo k3s ctr images import api-image.tar

# Deploy API
kubectl apply -f cluster-config/api-deployment.yml
kubectl apply -f cluster-config/api-service.yml

echo "Deployment completed. Allow a few minutes for pods to start."
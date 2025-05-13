#!/bin/bash

# Install k3s
curl -sfL https://get.k3s.io | sh -

# Install Docker (for building images)
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl enable --now docker

# Install Helm
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
# mysql-k8s
MySQL Cluster Wiot360

# DevOps Practical Assessment

## Prerequisites
- EC2 instance with Ubuntu, 2vCPU, 4GB RAM, 30GB disk
- Open ports: 22 (SSH), 30080 (API), 30306 (MySQL)

## Setup
1. SSH into EC2.
2. Clone the repo.
3. Run:
```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh


devops-assessment/
├── cluster-config/
│   ├── mysql-values.yaml
│   ├── api-deployment.yaml
│   ├── api-service.yaml
│   └── web-secret.yaml
├── api/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── scripts/
│   └── deploy.sh
└── README.md

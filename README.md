<div align="center">
  <h1>🏥 Health Information System</h1>
  
  <p>A modern web-based healthcare management platform built with modern technologies</p>
  
  <div>
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
    <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes" />
    <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS" />
    <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
  </div>
</div>

## 📋 Overview

A comprehensive **Health Information System** built with **Django** and **PostgreSQL**, containerized using **Docker**, orchestrated with **Kubernetes**, and deployed to **AWS**. This system provides a scalable backend infrastructure to manage patient records, appointments, and healthcare-related data with enterprise-grade security and reliability.

---

## 📂 Project Structure

```
health_info_system/
├── .github/workflows/       # GitHub Actions CI/CD workflows
├── app/                     # Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/                    # Your main application logic
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── ...
├── kubernetes/              # K8s deployment manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── configmap.yaml
├── manage.py                # Django CLI entry point
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Docker multi-container setup
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (excluded in .gitignore)
└── README.md                # You're reading it 😄
```

---

## 🛠️ Technology Stack

| Layer               | Technology                      |
|---------------------|----------------------------------|
| **Framework**       | Django 4+                       |
| **Database**        | PostgreSQL 14+                  |
| **DevOps**          | Docker, GitHub Actions          |
| **Orchestration**   | Kubernetes (EKS)                |
| **Cloud Provider**  | AWS (EKS, RDS, S3, CloudFront)  |
| **CI/CD**           | GitHub Actions                  |
| **Language**        | Python 3.10                     |
| **OS**              | Ubuntu (Docker-based)           |
| **Monitoring**      | Prometheus, Grafana             |

---

## 🚀 Setup Instructions

### ✅ Prerequisites

- Python 3.10+
- Docker + Docker Compose
- kubectl CLI
- AWS CLI configured with appropriate permissions
- Helm (for Kubernetes package management)
- GitHub Account for Actions
- PostgreSQL 14+ (if running outside Docker)

---

### 🧪 Local Development

1. **Clone the repository:**

```bash
git clone https://github.com/njange/health_info_system.git
cd health_info_system
```

2. **Copy environment variables:**

```bash
cp .env.example .env
# Edit .env to match your local DB credentials
```

3. **Build and run using Docker Compose:**

```bash
docker-compose up --build
```

4. **Run migrations:**

```bash
docker-compose exec web python manage.py migrate
```

5. **Create superuser:**

```bash
docker-compose exec web python manage.py createsuperuser
```

6. **Access the app:**

- App: [http://localhost:8000](http://localhost:8000)
- Admin: [http://localhost:8000/admin](http://localhost:8000/admin)

---

### 🧪 Running Tests

```bash
docker-compose exec web python manage.py test
```

---

### ☁️ AWS Deployment with Kubernetes

#### 1. **Create EKS Cluster**

```bash
eksctl create cluster --name health-system-cluster \
  --region us-west-2 \
  --nodegroup-name standard-workers \
  --node-type t3.medium \
  --nodes 3 \
  --nodes-min 1 \
  --nodes-max 4
```

#### 2. **Configure AWS RDS PostgreSQL**

```bash
aws rds create-db-instance \
    --db-instance-identifier health-db \
    --db-instance-class db.t3.micro \
    --engine postgres \
    --master-username admin \
    --master-user-password <your-password> \
    --allocated-storage 20
```

#### 3. **Deploy to Kubernetes**

```bash
# Apply ConfigMap with environment variables
kubectl apply -f kubernetes/configmap.yaml

# Apply database credentials as a Secret
kubectl create secret generic db-credentials \
  --from-literal=username=admin \
  --from-literal=password=<your-password>

# Deploy the application
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/ingress.yaml
```

#### 4. **Configure Ingress Controller and TLS**

```bash
# Install AWS Load Balancer Controller
helm repo add eks https://aws.github.io/eks-charts
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  --set clusterName=health-system-cluster \
  --namespace kube-system

# Install cert-manager for TLS
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.9.1/cert-manager.yaml
```

#### 5. **Add Auto-Scaling**

```bash
kubectl autoscale deployment health-system --cpu-percent=70 --min=2 --max=10
```

#### 6. **Access the Application**

Once deployed, you can access the application via the Load Balancer URL:

```bash
kubectl get ingress
# Copy the ADDRESS field to access the application
```

---

### ⚙️ CI/CD Pipeline with GitHub Actions

This project uses **GitHub Actions** to automate the deployment workflow:

```yaml
name: Deploy to AWS EKS

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-west-2
    
    - name: Login to Amazon ECR
      id: login-ecr
      uses: aws-actions/amazon-ecr-login@v1
    
    - name: Build, tag, and push image to Amazon ECR
      env:
        ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
        ECR_REPOSITORY: health-system
        IMAGE_TAG: ${{ github.sha }}
      run: |
        docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
        docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
    
    - name: Update kube config
      run: aws eks update-kubeconfig --name health-system-cluster --region us-west-2
    
    - name: Deploy to EKS
      run: |
        kubectl set image deployment/health-system health-system=$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
        kubectl rollout status deployment/health-system
```

> Set up required secrets in your GitHub repository: **Settings > Secrets and variables > Actions**

---

## 📁 Environment Variables

### Local Development (`.env`)

| Variable Name        | Description                        |
|----------------------|------------------------------------|
| `DEBUG`              | Enable/disable debug mode          |
| `SECRET_KEY`         | Django secret key                  |
| `POSTGRES_DB`        | Database name                      |
| `POSTGRES_USER`      | PostgreSQL username                |
| `POSTGRES_PASSWORD`  | PostgreSQL password                |
| `POSTGRES_HOST`      | DB host (e.g., `db`)               |
| `POSTGRES_PORT`      | Port (default: 5432)               |

### Kubernetes (ConfigMap and Secrets)

| Variable Name        | Description                        | Storage Method |
|----------------------|------------------------------------| ---------------|
| `DEBUG`              | Always set to `False` in prod      | ConfigMap      |
| `SECRET_KEY`         | Django secret key                  | Secret         |
| `DB_NAME`            | RDS Database name                  | ConfigMap      |
| `DB_USER`            | Database username                  | Secret         |
| `DB_PASSWORD`        | Database password                  | Secret         |
| `DB_HOST`            | RDS endpoint                       | ConfigMap      |
| `DB_PORT`            | Port (default: 5432)               | ConfigMap      |
| `AWS_ACCESS_KEY_ID`  | For S3 media storage               | Secret         |
| `AWS_SECRET_KEY`     | For S3 media storage               | Secret         |
| `AWS_STORAGE_BUCKET` | S3 bucket name                     | ConfigMap      |

---

## 💾 Database Migrations in Kubernetes

To run migrations in the Kubernetes environment:

```bash
# Create a one-time job for migrations
kubectl create job --from=cronjob/health-system-migrations migrations-manual

# Check job status
kubectl get jobs

# View logs
kubectl logs job/migrations-manual
```

---

## 📊 Monitoring and Logging

### Prometheus and Grafana Setup

```bash
# Add Prometheus repository
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

# Install Prometheus
helm install prometheus prometheus-community/kube-prometheus-stack

# Access Grafana (default credentials: admin/prom-operator)
kubectl port-forward svc/prometheus-grafana 3000:80
```

### ELK Stack for Logging

```bash
# Add Elastic repository
helm repo add elastic https://helm.elastic.co

# Install ELK stack
helm install elasticsearch elastic/elasticsearch
helm install kibana elastic/kibana
helm install filebeat elastic/filebeat

# Access Kibana
kubectl port-forward svc/kibana-kibana 5601:5601
```

---

## 🔒 Security

- Secrets management via Kubernetes Secrets and AWS Secrets Manager
- NetworkPolicies to restrict pod-to-pod communication
- RBAC (Role-Based Access Control) for Kubernetes resources
- AWS Security Groups limiting access to RDS and other resources
- TLS termination at the ingress level with automatic certificate renewal
- Django security best practices (HTTPS-only, strict content security policy)
- Regular security updates via automated CI/CD pipeline

---

## 🔄 Disaster Recovery

### Backup Strategy

- Automated PostgreSQL backups via AWS RDS snapshots (daily)
- Media/static files backed up from S3 to Glacier weekly
- Kubernetes state backed up using Velero

### Recovery Process

```bash
# Restore RDS from snapshot
aws rds restore-db-instance-from-db-snapshot \
    --db-instance-identifier health-db-restored \
    --db-snapshot-identifier health-db-snapshot

# Update Kubernetes secrets with new endpoint
kubectl edit secret db-credentials

# Restart deployments to use new database
kubectl rollout restart deployment health-system
```

---

## 👥 Contributing

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📚 License

MIT License © 2025 Njange

---

## 🙋‍♂️ Need Help?

If you have questions, feel free to open an [issue](https://github.com/njange/health_info_system/issues) or contact the maintainer.
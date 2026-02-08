# Todo App Kubernetes Deployment

## Build Docker image
eval $(minikube -p minikube docker-env)
docker build -t todo-app:1.0 ./app

## Deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

## Verify
kubectl get pods
kubectl get svc
minikube service todo-service --url

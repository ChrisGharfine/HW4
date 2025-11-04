pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ChrisGharfine/HW4'
            }
        }

        stage('Build in Minikube Docker') {
            steps {
                bat '''
                call minikube docker-env --shell=cmd > docker_env.bat
                call docker_env.bat
                docker build -t mydjangoapp:latest .
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat '''
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                kubectl rollout status deployment/django-deployment
                '''
            }
        }
    }
}

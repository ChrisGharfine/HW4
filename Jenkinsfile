pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ChrisGharfine/HW4.git'
            }
        }

        stage('Build in Minikube Docker') {
            steps {
                bat '''
                call minikube docker-env --shell=cmd > docker_env.bat
                call docker_env.bat
                cd mymovie
                docker build -t mydjangoapp:latest .
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat '''
                cd mymovie
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                kubectl rollout status deployment/django-deployment
                '''
            }
        }
    }
}

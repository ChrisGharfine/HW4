pipeline {
    agent any

    environment {
        // Your image name
        IMAGE_NAME = "mydjangoapp:latest"
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
                echo Setting up Minikube Docker environment...
                call minikube docker-env --shell=cmd > docker_env.bat
                call docker_env.bat

                echo Switching to mymovie directory...
                cd mymovie

                echo Building Docker image from GitHub code...
                docker build -t mydjangoapp:latest .

                echo Docker build completed successfully!
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat '''
                echo Applying Kubernetes deployment and service...
                cd mymovie
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml

                echo Deployment and service applied successfully!
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment completed successfully!"
        }
        failure {
            echo "❌ Deployment failed. Please check the Jenkins logs."
        }
    }
}

pipeline {
    agent any

    environment {
        DOCKER_USER = "thisispawankumar"
        IMAGE_NAME = "lab5"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'YOUR_GITHUB_REPO_URL'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install pandas scikit-learn joblib'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 scripts/train.py'
            }
        }

        stage('Print Metrics') {
            steps {
                sh '''
                echo "===== MODEL METRICS ====="
                cat metrics.json
                echo "Name: Pawan"
                echo "Roll No: 2022BCS0061"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_USER/$IMAGE_NAME:v1 .'
            }
        }

        stage('Login Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'TOKEN')]) {
                    sh 'echo $TOKEN | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_USER/$IMAGE_NAME:v1'
            }
        }
    }
}
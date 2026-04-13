pipeline {
    agent any

    environment {
        DOCKER_USER = "thisispawankumar"
        IMAGE_NAME = "lab4"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install pandas scikit-learn joblib
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . venv/bin/activate
                python scripts/train.py
                '''
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
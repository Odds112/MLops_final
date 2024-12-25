pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ml_project_final"
        REGISTRY = "docker.io/odds112"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Model Training') {
            steps {
                sh 'python src/train.py'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --junitxml=results.xml'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker tag $DOCKER_IMAGE $REGISTRY/$DOCKER_IMAGE:latest'
                sh 'docker push $REGISTRY/$DOCKER_IMAGE:latest'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'results.xml', fingerprint: true
        }
        failure {
            mail to: 'vitalik.zalozhnyj@gmail.com',
                 subject: 'Build Failed',
                 body: 'Please check Jenkins for details.'
        }
    }
}

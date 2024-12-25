pipeline {
    agent any

    environment {
        DOCKER_USERNAME = credentials('docker-credentials')
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
                sh '. venv/bin/activate && python src/train.py'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/ --junitxml=results.xml'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                script {                    
                    withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    }
                }
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                // Сборка Docker-образа
                sh 'docker build -t odds112/mlops_final .'
                // Тегирование образа
                sh 'docker tag odds112/mlops_final docker.io/odds112/mlops_final:latest'
                // Загрузка образа в Docker Hub
                sh 'docker push docker.io/odds112/mlops_final:latest'
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

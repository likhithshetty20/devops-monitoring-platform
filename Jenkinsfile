pipeline {
    agent any

    stages {

        stage('Clone Verification') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -f docker/Dockerfile -t devops-monitoring:v1 .'
            }
        }

    }
}

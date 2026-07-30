pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-monit"
        CONTAINER_NAME = "devops-app"
        DOCKERHUB_USERNAME = "likhith2"
    }
    

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build \
                -f docker/Dockerfile \
                -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Tag Docker Image') {
           steps {
               sh '''
               docker tag ${IMAGE_NAME}:${BUILD_NUMBER} \
               ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER}
               '''
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f ${CONTAINER_NAME} || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d \
                --name ${CONTAINER_NAME} \
                -p 5000:5000 \
                ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }

        stage('Push Docker Image') {
           steps {
               withCredentials([usernamePassword(
               credentialsId: 'dockerhub',
               usernameVariable: 'DOCKER_USER',
               passwordVariable: 'DOCKER_PASS'
            )]) {

                 sh '''
                 echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                 docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER}

                 docker logout
                 '''
                }
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl http://localhost:5000/health'
            }
        }
    }
}

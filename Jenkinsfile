pipeline {
    agent {
        label 'prod-vlan10-main'
    }

    environment {
        GIT_REPO = 'https://github.com/DennisWu0/Jenkin-color-web.git'
        WORK_DIR = '/opt/jenkins/color-web'

        REGISTRY = '192.168.217.100:5000'
        IMAGE_NAME = 'color-web'
        IMAGE_TAG = "${BUILD_NUMBER}"

        SERVER = '192.168.217.120'
    }

    stages {

        stage('Clone Source') {
            steps {
                sh """
                    rm -rf ${WORK_DIR}
                    git clone ${GIT_REPO} ${WORK_DIR}
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                dir("${WORK_DIR}") {
                    sh """
                        docker compose build
                    """
                }
            }
        }

        stage('Push Image') {
            steps {
                sh """
                    docker tag ${IMAGE_NAME}:latest ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker push ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage('Deploy Agent 1') {
            agent {
                label 'prod-vlan30-colorweb'
            }

            steps {
                sh """
                    docker pull ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}

                    docker rm -f color-web || true

                    docker run -d \
                        --name color-web \
                        -p 5001:5001 \
                        
                        -e DB_HOST= ${SERVER}\
                        -e DB_NAME=demo \
                        -e DB_USER=postgres \
                        -e DB_PASS=postgres \
                        
                        ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }
    }
}

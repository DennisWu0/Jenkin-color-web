pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo "Cloning repository from GitHub..."
                checkout scm
            }
        }

        stage('Test Connection') {
            steps {
                echo "Jenkins is successfully connected to GitHub!"
            }
        }

        stage('Show Git Info') {
            steps {
                sh '''
                    echo "Commit info:"
                    git log -1
                '''
            }
        }
    }
}

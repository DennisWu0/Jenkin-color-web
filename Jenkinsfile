pipeline {
    agent prod-vlan30-colorweb

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
                sh '''
                        echo "hello from agent" > test.txt
                        ls -l
                    '''
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

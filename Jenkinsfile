pipeline {
    agent any

    stages {
        stage('Build') {
            def dockerHome = tool 'my_docker'
            env.PATH = "${dockerHome}/bin:${env.PATH}"
            steps {
                sh '''
                  docker --version
                  docker compose version
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

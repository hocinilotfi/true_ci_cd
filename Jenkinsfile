
pipeline{
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('permissions setup') {
            steps {
                sh "chmod +x build.sh"
                sh "chmod +x deploy_integration.sh"

            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }
        stage('build') {
            steps {
                sh "./build.sh"
            }
        }
        stage('Deploy to Integration') {
            steps {
                sh "./deploy_integration.sh"
            }
        }
    }
}

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
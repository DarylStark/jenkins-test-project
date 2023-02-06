pipeline {
    agent any

    stages {
        stage('Set exection permissions to pipeline scripts')
        {
            steps {
                sh 'chmod +x jenkins/*.sh'
            }
        }

        stage('Install tools for Python3 Virtual Environment') {
            steps {
                sh 'jenkins/01-install-tools.sh'
            }
        }

        stage('Create Python3 Virtual Environment') {
            steps {
                sh 'jenkins/02-create-environment.sh'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'jenkins/03-install-dependencies.sh'
            }
        }

        stage('Unit testing') {
            steps {
                sh 'jenkins/04-testing.sh'
            }
        }
    }
}


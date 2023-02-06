pipeline {
    agent any

    stages {
        stage('Create Python3 environment') {
            steps {
                sh 'pip3 install --user --upgrade pip'
                sh 'pip3 install --user virtualenv'
                sh 'python3 -m venv env'
            }
        }

        stage('Activate Virtual environment') {
            steps {
                sh '. env/bin/activate'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Unit testing') {
            steps {
                echo '=== Running unit tests ==='
            }
        }
    }
}


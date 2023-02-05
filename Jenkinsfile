pipeline {
    agent any

    stages {
        stage('Install Python3 and Python3-venv') {
            steps {
                apt install python3 python3-venv
            }
        }

        stage('Create Python3 environment') {
            steps {
                python3 -m venv env
                source env/bin/activate
            }
        }

        stage('Install dependencies') {
            steps {
                pip3 install -r requirements.txt
            }
        }

        stage('Unit testing') {
            steps {
                echo '=== Running unit tests ==='
            }
        }
    }
}


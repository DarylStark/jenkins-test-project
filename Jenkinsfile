pipeline {
    agent any

    stages {
        stage('BUILD - Set exection permissions to pipeline scripts')
        {
            steps {
                sh 'chmod +x jenkins/*.sh'
            }
        }

        stage('BUILD - Install tools for Python3 Virtual Environment') {
            steps {
                sh 'jenkins/01-install-tools.sh'
            }
        }

        stage('BUILD - Create Python3 Virtual Environment') {
            steps {
                sh 'jenkins/02-create-environment.sh'
            }
        }

        stage('BUILD - Install dependencies') {
            steps {
                sh 'jenkins/03-install-dependencies.sh'
            }
        }

        stage('TEST - Unit testing') {
            steps {
                sh 'jenkins/04-testing.sh'
            }
        }

        stage('CI - Integrate branch') {
            steps {
                script {
                    if (env.BRANCH_NAME != 'main') {
                        sh 'jenkins/05-merging.sh'
                    } else {
                        echo 'Already on the main branch: nothing to do'
                    }
                }
            }
        }

        stage('TEST - Unit testing after merging') {
            steps {
                script {
                    if (env.BRANCH_NAME != 'main') {
                        sh 'jenkins/04-testing.sh'
                    } else {
                        echo 'Already on the main branch: nothing to do'
                    }
                }
            }
        }
    }
}


pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'pip install selenium'
                bat 'docker-compose build'
            }
        }

        stage('Run') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                dir('test') {
                    bat 'python.exe e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                bat 'docker-compose down'
                bat 'docker-compose push'
            }
        }
    }
}

pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'myflaskapp:latest'
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Feekree/myflaskapp.git'
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint Code') {
            steps {
                // Check code quality with pylint
                sh 'pylint app.py'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run tests using pytest
                sh 'python -m unittest discover'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Deploy') {
            steps {
                // Run the Docker container
                sh 'docker run -d -p 5000:5000 ${DOCKER_IMAGE}'
            }
        }

        stage('Post-Build Actions') {
            steps {
                // Clean up Docker resources (optional)
                sh 'docker system prune -f'
            }
        }
    }

    post {
        always {
            // Archive test reports, logs, etc.
            archiveArtifacts artifacts: '**/tests/*.py', allowEmptyArchive: true
        }
    }
}

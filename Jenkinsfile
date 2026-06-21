    pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git branch: 'master',
                    url: 'https://github.com/Manish3434/jenkins.git'
            }
        }

        stage('Build Docker Image') {

            steps {

                sh '''
                 docker build -t manishkumar34/manish-library-app:latest .
                '''
            }
        }

        stage('Docker Login') {

            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {

                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {

            steps {

                sh '''
                 docker push manishkumar34/manish-library-app:latest
                '''
            }
        }

        stage('Deploy Container') {

            steps {

                sh '''
                 docker rm -f library-app || true

                docker run -d \
                --name library-app \
                -p 8000:8000 \
                manishkumar34/manish-library-app:latest
                '''
            }
        }
    }
} 

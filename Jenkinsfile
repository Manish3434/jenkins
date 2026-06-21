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
                sudo docker build -t manishkumar34/manish-library-app:latest .
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
                    echo $DOCKER_PASS | sudo docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {

            steps {

                sh '''
                sudo docker push manishkumar34/manish-library-app:latest
                '''
            }
        }

        stage('Deploy Container') {

            steps {

                sh '''
                sudo docker rm -f library-app || true

                sudo docker run -d \
                --name library-app \
                -p 8000:8000 \
                manishkumar34/manish-library-app:latest
                '''
            }
        }
    }
} 


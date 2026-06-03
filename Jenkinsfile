pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git branch: 'master',
                url: 'https://github.com/Manish3434/jenkins.git'
            }
        }

        stage('Install Dependencies') {

            steps {

                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Migrate') {

            steps {

                sh '''
                . venv/bin/activate
                python manage.py makemigrations
                python manage.py migrate
                python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Deploy') {

            steps {

                sh '''
                nohup venv/bin/gunicorn \
--workers 4 \
--bind 0.0.0.0:8000 \
library_project.wsgi:application \
> gunicorn.log 2>&1 &               
'''
            }
        }
    }
}



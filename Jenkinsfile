pipeline{
    agent any
    stages{
        stage('Git checkout'){
            steps{
                git branch: 'develop', credentialsId: 'ssh-remote-web', url: 'https://github.com/nambh911/web_app.git'
            }
        }
        stage('Execute test web-app'){
            steps{
                sh 'cd /home/nambh6/web_app'
                sh 'python3 manage.py test'
            }
        }
        stage('Build docker image'){
            steps{
                sh 'docker build -t web-app .'
            }
        }
        stage('Run docker container'){
            steps{
                sh 'docker run -d --name web-django -p 8000:8000 web-app'
                sh 'docker ps'
            }
        }
    }
}

pipeline{
    agent any
    stages{
        stage('Git checkout'){
            steps{
                git branch: 'develop', credentialsId: 'ssh-remote-web', url: 'https://github.com/nambh911/web_app.git'
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
            }
        }
    }
}

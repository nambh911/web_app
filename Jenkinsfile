pipeline{
    agent any
    stages{
        stage('Git checkout'){
            steps{
                git branch: 'develop', credentialsId: 'ssh-remote-web', url: 'https://github.com/nambh911/web_app.git'
            }
        }
        stage('SSH server and Execute test web-app'){
            steps{
                sshagent(['ssh-remote']) {
                    sh 'ssh -o StrictHostKeyChecking=no -l cloudbees 10.17.143.117 python3 manage.py test'
                }
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

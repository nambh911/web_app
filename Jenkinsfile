pipeline{
    agent any
    stages{
        stage('Git checkout'){
            steps{
                git branch: 'master', credentialsId: 'ssh-remote-web', url: 'https://github.com/nambh911/web_app.git'
            }
        }
        stage('SSH server and Execute test web-app'){
            steps{
                sshagent(['ssh-root-ubuntu']) {
                    sh 'ssh -o StrictHostKeyChecking=no -l nambh6 10.17.143.117 python3 /home/nambh6/web_app/web/manage.py test'
                }
            }
        }
        stage('Build docker image'){
            steps{
                dir('./web') {
                    sh 'docker build -t web-app .'
                }
            }
        }
        stage('Run docker container'){
            steps{
                sh 'docker run -d -p 8000:8000 web-app'
                sh 'docker ps'
            }
        }
    }
}

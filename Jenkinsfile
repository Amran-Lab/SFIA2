pipeline{
    agent any
    stages{
        stage('Dev Test Env'){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                
                sh 'ansible-playbook playbook.yml -i inventory.cfg'
                sh 'docker stack deploy --compose-file docker-compose.yml stackdemo'
                sh 'echo $SQLHOST'
                
                

            }
        }

    }
}
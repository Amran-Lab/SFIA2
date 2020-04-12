pipeline{
    agent any
    stages{
        stage('Dev Test Env'){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh 'export ANSIBLE_HOST_KEY_CHECKING=False'
                sh 'sudo usermod -a -G docker jenkins'
                sh 'sudo ansible-playbook playbook.yml -i inventory.cfg'
                sh 'sudo docker stack deploy --compose-file docker-compose.yml stackdemo'
                sh 'echo $SQLHOST'
                
                

            }
        }

    }
}
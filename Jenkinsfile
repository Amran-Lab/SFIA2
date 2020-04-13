pipeline{
    agent any
    stages{
        stage('Dev Test Env'){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh 'export ANSIBLE_HOST_KEY_CHECKING=False'                
                sh 'sudo ansible-playbook playbook.yml -i inventory.cfg'
                sh 'sudo docker stack deploy --compose-file docker-compose.yml stackdemo'
                sh 'echo $SQLHOST'
                sh 'sudo docker service ls'
                sh 'source /var/jenkins_home/workspace/dockerline/venv/bin/activate'
                sh 'pip3 install flask'
                sh 'pip3 install flask_mysqldb'
                sh 'pip3 install -U pytest'
                sh 'pip3 install urllib3'
                sh 'pip3 install coverage'
                sh 'py.test /var/jenkins_home/workspace/dockerline/service_1/testing.py --cov='service_1' --cov-report term-missing'
                
                

            }
        }

    }
}
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
                
                sh 'pip3 install flask'
                sh 'pip3 install flask_mysqldb'
                sh 'pip3 install -U pytest'
                sh 'pip3 install urllib3'
                sh 'pip3 install coverage'
                sh 'pip3 install pytest-cov'
                
                sh 'python3 -m pytest service_1/testing.py  --cov="service_1"'

                sh 'echo $MYSQL_DB'
                
                

            }
        }

    }
}
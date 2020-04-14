# QA-Project
## Index

[Brief](#brief)
   * [My Solution](#mysolution)
   * [WireFrame](#WireFrame)
   


[Risk Assessment](#RA)

[Trello and Planning](#TAP)
  * [Trello Before](#Tap1)
  * [Trello After](#Tap2)

[Deployment](#Deploy)
  * [Pipline](#Pipeline)

[Testing](#Testing)

[Retrospective](#Retro)  

[How To Run](#Run)  

[Problems](#Problems)

<a name="brief"></a>

### Brief

The Brief was to create a CI/CD pipeline using Jenkins andsible and docker.It should also cnsist of 4 micro-services with data being persisted by sql.

I decided to make a higher/lower game with a deck of cards. With service once containing front end, service 2 picking a card, service 3 giving points/message and service 4 comapring what user picked to what happened(the calculations).

### WireFrame

![GitHub Logo](https://github.com/Amran-Lab/RDME/blob/master/WireFrame.PNG?raw=true)

I plan to have an apllication that gives you a card and you can pick higher or lower and compares it against a new card.
You can submit you name and last go to sql.


<a name="RA"></a>

### Risk Assessment

| Risk Assessment                                 | Risk Factor | Mitigating                                        | New Risk Factor |
|-------------------------------------------------|-------------|---------------------------------------------------|-----------------|
| 1.Corrupted Files                                 | 8/10        | Online Version Control                            | 3/10            |
| 2.Deleted Files                                   | 6/10        | Online Version Control                            | 1/10            |
| 3.Losing Git Password                             | 9/10        | Have Email Recovery                               | 2/10            |
| 4.Falling Sick                                    | 9/10        | Maintain Health/Visiting Doc/Sanitizing/Isolating | 7/10            |
| 5.Data of Site Leaked                             | 3/10        | Hashing/Storing Sensitive Information In Secure Locations             | 1/10            |
| 6.Not Understanding Own Code                      | 7/10        | Good Commenting                                   | 5/10            |
| 7.Underestimation of the time/resource commitment | 6/10        | Trello Board                                      | 4/10            |
| 8.Running out of Money for Cloud                  | 3/10        | Pausing instance when not in use/Not Making Many VMS                  | 2/10            |
| 9.Getting Hacked                                  | 7/10        | Strong password                                   | 4/10            |
| 10.Open Port                                       | 4/10        | Make Port only accessible for public on one vm others closed to public                                  | 4/10            |
| 11.GCP Going Down                                  | 5/10        | Out Of Control                                   | 5g/10            |



![GitHub Logo](https://github.com/Amran-Lab/RDME/blob/master/rmatrix.PNG?raw=true)

\
\
\
\
\



<a name="TAP"></a>
<a name="TAP1"></a>

### Trello and Planning

### Trello Before

![GitHub Logo](https://github.com/Amran-Lab/RDME/blob/master/Trellob4.PNG?raw=true)




<a name="TAP2"></a>

### Trello After

![GitHub Logo](https://github.com/Amran-Lab/RDME/blob/master/TrelloAf.PNG?raw=true)



For my planning I used Trello. I have moved over tasks when completed to done or when something is ongoing such as the readme it is in the doing tab. I also have a tab of
for the user stories and requirements, to make sure I am meeting the requirements.



<a name="Deploy"></a>
<a name="Pipeline"></a>

### Deployment

![GitHub Logo](https://github.com/Amran-Lab/RDME/blob/master/Diagram1.png?raw=true)

Program will be coded in vscode using python-flask and version controlled on GitHub. You can build with jenkins with the latest version. This will be ran on a GCP Virtual Machine which will be connected to a GCP MYSQL database. There are 4 services which are in a network.
Service 1 gets card info from service 2 and service 4 gets player choice and new card info from service 1 and sends back information to
service 1 depending on the choice and outcome the message will be altered by service 3.

### NGINX

Nginx is there as a reverse proxy it works as an extra layer of security so no one directly accesses the container. It also means
I only need to oper port 80 to the public for one VM.


<a name="Testing"></a>

### Testing



![GitHub Logo](https://github.com/Amran-Lab/RDME/blob/master/coverage1.PNG?raw=true)

I tested service 1 because the main stuff happen there I also tested for URL and DB.

<a name="Retrospective"></a>

### Retrospective

### What Went Well?
+ CI/CD Pipleline with jenkins
+ Working ansible and docker compose
+ Code easy to read
+ Good Version Control

### Problems
+ GCP going down
+ ssh keys not working (fixed by changing permission of priv ssh file)
+ ssh key checking (fixed check how to run for further details)
+ service 4 uses global variables 
+ Entering Data to Database has some problems

### Future Improvements
+ merge service 4 to service 1
+ Better Looking Frontend
+ Full CRUD

<a name="Run"></a>

### How To Run

1. Download Jenkins for Ubuntu (turorial https://jenkins.io/doc/book/installing/#debianubuntu)
2. Set Up firewall port 5000 open to public on vm
3. Set Up mysql database
5. Create Pipeline
4. Create .env file with database info to pass to conatainer written in form in the jenkins workspace for that pipeline
    ```
        MYSQl_HOST=xxx...
        MYSQl_PASSWORD=xxx...
        MYSQl_USER=xxx...
        MYSQl_DB=xxx...
 
 
5. Create an inventory.cfg file
    ```[servers]
        localhost ansible_connection = local ansible_user=.... ansible_ssh_private_key_file= Location of File
        Host Address ansible_connection = ssh ansible_user=.... ansible_ssh_private_key_file= Location of File
        Host Address ansible_connection = ssh ansible_user=.... ansible_ssh_private_key_file= Location of File
        [swarm-manager]
        localhost ansible_connection=local       
        [swarm-workers]
        Host Address ansible_connection = ssh ansible_user=.... ansible_ssh_private_key_file= Location of File
        Host Address ansible_connection = ssh ansible_user=.... ansible_ssh_private_key_file= Location of File
 6. Give Jenkins sudo access
 7. export ANSIBLE_HOST_KEY_CHECKING=False or change it at /etc/ansible/ansible.cfg (..https://stackoverflow.com/questions/23074412/how-to-set-host-key-checking-false-in-ansible-inventory-file)
 7. Run Pipeline


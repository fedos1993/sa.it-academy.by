## Homework Assignment 1: Configuration Management

[Ansible config](ansible.cfg)

[Playbook](nginx_playbook.yaml)

[Inventory](inv.yaml)

Templates:

[HTML](templates/index.j2)

[Virtualhost config](templates/config.j2)

#### Playbook outpoot
```shell
PLAY [Configure and deploy Nginx] ***************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************
Вторник 07 января 2025  10:26:07 +0000 (0:00:00.051)       0:00:00.051 ********
ok: [nginx]

TASK [Install Nginx] ****************************************************************************************************************************************
Вторник 07 января 2025  10:26:10 +0000 (0:00:03.519)       0:00:03.571 ********
ok: [nginx]

TASK [Manage the Nginx Proccess] ****************************************************************************************************************************
Вторник 07 января 2025  10:26:13 +0000 (0:00:03.347)       0:00:06.919 ********
changed: [nginx]

TASK [Create directories for virtual hosts] *****************************************************************************************************************
Вторник 07 января 2025  10:26:15 +0000 (0:00:01.954)       0:00:08.874 ********
changed: [nginx] => (item={'name': 'site1'})
changed: [nginx] => (item={'name': 'site2'})

TASK [Create index.html] ************************************************************************************************************************************
Вторник 07 января 2025  10:26:18 +0000 (0:00:02.188)       0:00:11.062 ********
changed: [nginx] => (item={'name': 'site1'})
changed: [nginx] => (item={'name': 'site2'})

TASK [Create Nginx config] **********************************************************************************************************************************
Вторник 07 января 2025  10:26:22 +0000 (0:00:04.322)       0:00:15.385 ********
changed: [nginx] => (item={'name': 'site1'})
changed: [nginx] => (item={'name': 'site2'})

TASK [Enable virtual host by creating link] *****************************************************************************************************************
Вторник 07 января 2025  10:26:25 +0000 (0:00:03.532)       0:00:18.917 ********
changed: [nginx] => (item={'name': 'site1'})
changed: [nginx] => (item={'name': 'site2'})

TASK [Setting /etc/hosts] ***********************************************************************************************************************************
Вторник 07 января 2025  10:26:27 +0000 (0:00:02.023)       0:00:20.941 ********
changed: [nginx] => (item={'name': 'site1'})
changed: [nginx] => (item={'name': 'site2'})

TASK [Check syntax errors in Nginx files] *******************************************************************************************************************
Вторник 07 января 2025  10:26:30 +0000 (0:00:02.196)       0:00:23.137 ********
changed: [nginx]

TASK [Reloaded Nginx] ***************************************************************************************************************************************
Вторник 07 января 2025  10:26:31 +0000 (0:00:01.295)       0:00:24.433 ********
changed: [nginx]

TASK [Check sites] ******************************************************************************************************************************************
Вторник 07 января 2025  10:26:33 +0000 (0:00:01.655)       0:00:26.088 ********
ok: [nginx] => (item={'name': 'site1'})
ok: [nginx] => (item={'name': 'site2'})

TASK [Print content of sites] *******************************************************************************************************************************
Вторник 07 января 2025  10:26:35 +0000 (0:00:02.422)       0:00:28.510 ********
ok: [nginx] => (item=http://site1) => {
    "msg": "Content from http://site1: <html>\n<head>\n    <title>site1</title>\n</head>\n<body>\n    <h1>Welcome to site1</h1>\n    <p>Homework 06.Ansible Workshop</p>\n    <p>Host: ws-7</p>\n</body>\n</html>\n"
}
ok: [nginx] => (item=http://site2) => {
    "msg": "Content from http://site2: <html>\n<head>\n    <title>site2</title>\n</head>\n<body>\n    <h1>Welcome to site2</h1>\n    <p>Homework 06.Ansible Workshop</p>\n    <p>Host: ws-7</p>\n</body>\n</html>\n"
}

PLAY RECAP **************************************************************************************************************************************************
nginx                      : ok=12   changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
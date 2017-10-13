AIX & PowerVM automation with Ansible
#####################################

:date: 2017-10-12 23:30
:modified: 2017-10-13 16:30
:tags: aix, ansible, automation, modules, setup, howto
:category: Automation Ansible AIX
:authors: Kairo Araujo
:summary: Using Ansible to manage AIX/PowerVM servers


**On this post I will show how to setup Ansible control with special modules and
facts for AIX and give you some useful examples.**

Ansible is a simple and powerful open source tool to automate repeated tasks
for the system administrator, making life easier.
The biggest advantage of Ansible, in my opinion is that Ansible is agent less
and only has two requirements, SSH and Python on the target.

I have been playing a lot with Ansible to automate AIX and I also have been
writing some contributions to the project to make Ansible work smooth with AIX.

.. contents:: Table of Contents
   :depth: 3

Overview
========

For that I’m using a Red Hat Linux 7.4 as Ansible control to manage my AIX 6.1, 7.1 and 7.2 servers/nodes.
My servers/nodes are AIXs and Linuxes boxes.

Special modules/facts for AIX
-----------------------------

I have been writing some AIX modules and core (facts) to make it smoother  for AIX.
All codes I have submitted Pull Requests to Ansible project, my goal is to have it on next versions of Ansible.
While it is not available on the official Ansible repository — I hope to have something on 2.5 —
I created a repository on my Github to make it include this support to current stable version 2.4 .

https://github.com/kairoaraujo/ansible-AIX-support

+---------+---------------+------------------------------------------+
| Type    | Name          | Description                              |
+=========+===============+==========================================+
| module  | aix_lvg       | AIX Logical Volume management            |
+---------+---------------+------------------------------------------+
| module  | aix_filesystem| AIX Files system mamagement (LVM and NFS)|
+---------+---------------+------------------------------------------+
| module  | mksysb        | AIX rootvg backup with mksysb            |
+---------+---------------+------------------------------------------+
| module  | installp      | AIX package management                   |
+---------+---------------+------------------------------------------+
| utils   | aix           | AIX hardware Ansible facts               |
+---------+---------------+------------------------------------------+



Ansible Control setup
=====================

Operational System: Red Hat Linux 7.4
Ansible: 2.4
Python: 2.7
Custom modules and core for AIX

Operational System installation and preparation
-----------------------------------------------

The Operation System (OS) installation follows a basic installation for Red hat 7.4 as a server.

Requisites for Ansible Control server installation

1. Validate if Python is already installed

.. code-block:: bash

    [root@ansible-cs ~]# python --version
    Python 2.7.5


2. Install PIP and python devel

.. code-block:: bash

    [root@ansible-cs ~]# yum install python-pip python-devel

3. Upgrade pip

.. code-block:: bash

    [root@ansible-cs ~]# pip install --upgrade pip


Ansible 2.4 Installation
-----------------------------------------------

The installation can be done using PIP

1. Run PIP to install

.. code-block:: bash

    [root@ansible-cs ~]# pip install ansible

2. Check Ansible Version

.. code-block:: bash

    [root@ansible-cs ~]# ansible --version
    ansible 2.4.0.0
        config file = None
        configured module search path = [u'/root/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
        ansible python module location = /usr/lib/python2.7/site-packages/ansible
        executable location = /bin/ansible
        python version = 2.7.5 (default, May  3 2017, 07:55:04) [GCC 4.8.5 20150623 (Red Hat 4.8.5-14)]


Ansible AIX modules/support installation
----------------------------------------

1. Download from github

https://github.com/kairoaraujo/ansible-aix-support/releases/download/0.0.2/ansible-aix-support-0.0.2.tar.gz

Extract the file

.. code-block:: bash

    [root@ansible-cs ~]# tar xvzf ansible-aix-support-0.0.2.tar.gz

Or download using git

.. code-block:: bash

    [root@ansible-cs ~]# git clone https://github.com/kairoaraujo/ansible-aix-support

2. Go to the directory

.. code-block:: bash

    [root@ansible-cs ~]# cd ansible-aix-support

3. Run installation script

.. code-block:: bash

    [root@ansible-cs ansible-aix-support]# sh install-ansible-aix-support.sh
    Starting installation of Ansible AIX support

    [INFO] Checking Ansible installation.
    [INFO] Ansible found.
    [INFO] Checking Ansible installation
    [INFO] Version compatible.
    [INFO] Backup file /usr/lib/python2.7/site-packages/ansible/module_utils/facts/hardware/aix.py
    [INFO] Adding /usr/lib/python2.7/site-packages/ansible/module_utils/facts/hardware/aix.py
    [INFO] Adding /usr/lib/python2.7/site-packages/ansible/modules/packaging/os/installp.py
    [INFO] Adding /usr/lib/python2.7/site-packages/ansible/modules/system/aix_filesystem.py
    [INFO] Adding /usr/lib/python2.7/site-packages/ansible/modules/system/aix_lvg.py
    [INFO] Adding /usr/lib/python2.7/site-packages/ansible/modules/system/mksysb.py
    [INFO] Finished.

3. Verifying

.. code-block:: bash

    [root@ansible-cs ~]# ansible-doc aix_lvg


Ansible Control Setup
=====================

Generating keys
---------------

On Ansible Control you need to generate the keys to be used by targets (AIX/VIOSes).

.. code-block:: bash

    [root@ansible-cs ~]# ssh-keygen
    Generating public/private rsa key pair.
    Enter file in which to save the key (/root/.ssh/id_rsa):
    Created directory '/root/.ssh'.
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /root/.ssh/id_rsa.
    Your public key has been saved in /root/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:FsuneRLg7Ugqk4rp12Goip8GaQAaBEFNIANZCgSU1l8 root@ansible-cs
    The key's randomart image is:
    +---[RSA 2048]----+
    |^XB.             |
    |*= o   E         |
    |=.  . o .        |
    |o    o + o       |
    |..  . o S .      |
    |o. o = + =       |
    |..= + o = .      |
    |o+.= .   o       |
    |O++              |
    +----[SHA256]-----+


Ansible targets (AIX/VIOS) setup
================================

Ansible is agentless, this means that Ansible installation is not required.
Ansible requires just two things: SSH (probably you already have it) and Python.

Installing Python on AIX
------------------------

So, to install Python on AIX I recommend downloading AIX Python package from http://www.aixtools.net/index.php/python

Remark: The only requisite is >= openssl.base.rte.1.0.1.515

1. Send the package to AIX boxes on /tmp

2. Install using installp command

.. code-block:: bash

    # installp -aF -XY -d /tmp/ aixtools.python

4. Create the symbolic links

.. code-block:: bash

    # ln -s /opt/bin/python /usr/bin/python
    # ln -s /opt/bin/pip /usr/bin/pip

3. Test it

.. code-block:: bash

    # python python --version
    Python 2.7.12


Distributing keys
-----------------

The easy way to distribute the SSH keys to the AIX/VIOS servers is using ssh-copy-id

If you cannot use keys with root to use SSH, Ansible supports sudo. This means that you can have another user to connect to AIX/VIOS and run Ansible with sudo. Check out http://docs.ansible.com/ansible/latest/become.html

In that case, you need to use ssh-copy-id to user that you want to perform Ansible connection and have properly sudoers configured.

On that example we are using root.

.. code-block:: bash

    [root@ansible-cs ~]# ssh-copy-id -i .ssh/id_rsa.pub root@lpar24
    [root@ansible-cs ~]# ssh-copy-id -i .ssh/id_rsa.pub root@lpar28
    (...)

Example from root to user ansible.

.. code-block:: bash

    [root@ansible-cs ~]# ssh-copy-id -i .ssh/id_rsa ansible@lpar24
    [root@ansible-cs ~]# ssh-copy-id -i .ssh/id_rsa ansible@lpar28
    (...)

Another way is to copy the .ssh/id_rsa.pub to the AIX LPAR to root the user home (or another user), inside .ssh/authorized_keys

Ansible Inventory and validation
================================

To perform Ansible in your environment an Inventory on Ansible Control is required.
The Inventory will have your target definitions, I encourage you to read it http://docs.ansible.com/ansible/latest/intro_inventory.html
You can also have a dynamic inventory, you can search about it ;)

Creating an inventory
---------------------

On this doc I created a simple inventory as example, including also a Linux server.

.. code-block:: bash

    [root@ansible-cs ~]# cat /etc/ansible_inventory
    # Global variables
    [all:vars]
    ansible_user=root

    [aix]
    lpar24
    lpar28

    [hacmp]
    lpar21
    lpar22

    [legacy]
    lpar23

    [linux]
    linux4


As you can see, I also included a Linux to show how you can manage both platforms together.

Checking configuration
----------------------

Let's check if our configuration is working well:

.. code-block:: bash

    [root@ansible-cs ~]# ansible -i /etc/inventory all -m ping
    lpar24 | SUCCESS => {
        "changed": false,
        "failed": false,
        "ping": "pong"
    }
    lpar28 | SUCCESS => {
        "changed": false,
        "failed": false,
        "ping": "pong"
    }
    lpar22 | SUCCESS => {
        "changed": false,
        "failed": false,
        "ping": "pong"
    }
    lpar23 | SUCCESS => {
        "changed": false,
        "failed": false,
        "ping": "pong"
    }
    lpar21 | SUCCESS => {
        "changed": false,
        "failed": false,
        "ping": "pong"
    }
    linux4 | SUCCESS => {
        "changed": false,
        "failed": false,
        "ping": "pong"
    }

Playbook example
----------------

Playbooks are configurations, deployments and tasks that you want to perform in a target host.
For more details, check out http://docs.ansible.com/ansible/latest/playbooks.html

My first example of playbook will be: Create a filesystem for images and install TSM software and generate a mksysb backup.
In details my tasks are:
- Logical Volume with 5GB (lvmksysb) Remark: (only for servers that I already have +5GB free on vg)
- Create a filesystem using lvmksysb (/mksysb/images)
- Install TSM software


My playbook:

.. code-block:: yml

    [root@ansible-cs ~]# cat /playbooks/pb-mksysb-tsm.yml
    ---
    - name: mksysb & tsm client install
      hosts: prd

      tasks:
        - name: Create LV (mksysblv) with 5GB
          aix_lvol:
            vg: rootvg
            lv: mksysblv
            size: 5G
            state: present
          register: lv_result
          when:
            - ansible_system == "AIX"

        - name: Create file system using mksysblv
          aix_filesystem:
            device: mksysblv
            filesystem: /mksysb/images
            state: present
          register: fs_result
          when:
            - lv_result.changed

        - name: Mount filesystem /mksysb/images
          aix_filesystem:
            filesystem: /mksysb/images
            state: mounted
          register: mount_result
          when:
            - fs_result.changed

        - name: Install TSM client
          installp:
            repository_path: /software/tsm/TSMCLI
            name: all
            state: present
          when:
            - ansible_system == "AIX"

        - name: Generate a mksysb on /mksysb/images
          mksysb:
            name: myserver
            storage_path: /mksysb/images
            exclude_files: yes
            exclude_wpar_files: yes
          when:
            - ansible_system == "AIX"
            - ansible_nodename == "lpar28"


Running the playbook
--------------------

.. code-block:: bash

    [root@ansible-cs ~]# ansible-playbook -i /etc/inventory /playbooks/pb-mksysb-tsm.yml -v

    PLAY [mksysb & tsm client install] **********************************************************************************************

    TASK [Gathering Facts] **********************************************************************************************************
    ok: [linux4]
    ok: [lpar28]
    ok: [lpar24]

    TASK [Create LV (mksysblv) with 5GB] ********************************************************************************************
    skipping: [linux4] => {"changed": false, "skip_reason": "Conditional result was False", "skipped": true}
    changed: [lpar28] => {"changed": true, "failed": false, "msg": "Logical volume mksysblv created."}
    changed: [lpar24] => {"changed": true, "failed": false, "msg": "Logical volume mksysblv created."}

    TASK [Create file system using mksysblv] ****************************************************************************************
    skipping: [linux4] => {"changed": false, "skip_reason": "Conditional result was False", "skipped": true}
    changed: [lpar28] => {"changed": true, "failed": false, "msg": "File system created successfully.\n5242516 kilobytes total disk space.\nNew File System size is 10485760\n", "state": "present"}
    changed: [lpar24] => {"changed": true, "failed": false, "msg": "File system created successfully.\n5242516 kilobytes total disk space.\nNew File System size is 10485760\n", "state": "present"}

    TASK [Mount filesystem /mksysb/images] ******************************************************************************************
    skipping: [linux4] => {"changed": false, "skip_reason": "Conditional result was False", "skipped": true}
    changed: [lpar28] => {"changed": true, "failed": false, "msg": "File system /mksysb/images mounted.", "state": "mounted"}
    changed: [lpar24] => {"changed": true, "failed": false, "msg": "File system /mksysb/images mounted.", "state": "mounted"}

    TASK [Install TSM client] *******************************************************************************************************
    skipping: [linux4] => {"changed": false, "skip_reason": "Conditional result was False", "skipped": true}
    changed: [lpar24] => {"changed": true, "failed": false, "msg": " Installed: all."}
    changed: [lpar28] => {"changed": true, "failed": false, "msg": " Installed: all."}

    TASK [Generate a mksysb on /mksysb/images] **************************************************************************************
    skipping: [lpar24] => {"changed": false, "skip_reason": "Conditional result was False", "skipped": true}
    skipping: [linux4] => {"changed": false, "skip_reason": "Conditional result was False", "skipped": true}
    changed: [lpar28] => {"changed": true, "failed": false, "msg": "\nCreating information file (/image.data) for rootvg.\n\nCreating list of files to back up \n.\nBacking up 80239 files........................\n\n80239 of 80239 files backed up (100%)\n0512-038 mksysb: Backup Completed Successfully.\n"}

    PLAY RECAP **********************************************************************************************************************
    linux4                     : ok=1    changed=0    unreachable=0    failed=0
    lpar24                     : ok=5    changed=4    unreachable=0    failed=0
    lpar28                     : ok=6    changed=5    unreachable=0    failed=0


Conclusion
==========

Ansible is simple tool that can helps a lot system administrators and DevOps to manage their environments.
In my humble opinion the Ansible documentation is nice and there are a lot of training, tutorials, webinars
that can help develop the skills about Ansible.

I will keep working on modules and more support between Ansible and AIX/PowerVM.

Suggestions are welcome. :)
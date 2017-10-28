New Ansible module AIX Devices
##############################

:date: 2017-10-28 17:30
:modified: 2017-10-28 17:30
:tags: aix, ansible, automation, modules, aix_devices
:category: Automation Ansible AIX
:authors: Kairo Araujo
:summary: New Ansible module to manage devices on AIX

Today I submitted a new pull request (PR) to Ansible Project with a new
module. The new module aix_devices makes easy discovers, defines, removes
and modifies attributes of AIX devices.

I also released this new module on my `Ansible AIX support
collections <https://github.com/kairoaraujo/ansible-aix-support>`_.
If you don't what is that, visit `my post about AIX modules
<http://kairo.eti.br/aix-powervm-automation-with-ansible.html>`_

I am very motivated to put AIX native supported on Ansible.

This module is very useful to manage devices, doing tuning, discovering new
adapters and also managing network and routing on AIX as it is configurable
directly on devices as ``enX`` and ``inet0``.

See below a collection of uses of this module:

.. code-block:: yml

    ---
    - name: Testing
      hosts: lpar22

      tasks:
        - name: Scan new devices.
          aix_devices:
            device: all
            state: present

        - name: Scan new virtual devices (vio0).
          aix_devices:
            device: vio0
            state: present

        - name: Removes ent2.
          aix_devices:
            device: ent2
            state: absent

        - name: Put device en2 in Defined
          aix_devices:
            device: en2
            state: defined

        - name: Removes ent4 (inexistent).
          aix_devices:
            device: ent4
            state: absent

        - name: Put device en4 in Defined (inexistent)
          aix_devices:
            device: en4
            state: defined

        - name: Put vscsi1 and children devices in Defined state.
          aix_devices:
            device: vscsi1
            recursive: yes
            state: defined

        - name: Removes vscsi1 and children devices.
          aix_devices:
            device: vscsi1
            recursive: yes
            state: absent

        - name: Changes en1 mtu to 9000 and disables arp.
          aix_devices:
            device: en1
            attributes: mtu=900,arp=off
            state: present

        - name: Configure IP, netmask and set en1 up.
          aix_devices:
            device: en1
            attributes: netaddr=192.168.0.100,netmask=255.255.255.0,state=up
            state: present

        - name: Adding IP alias to en0
          aix_devices:
            device: en0
            attributes: [
                "alias4=10.0.0.100,255.255.255.0"
                ]
            state: present

Output from this playbook

.. code-block:: shell


    # ansible-playbook -i /etc/inventory playbooks/test.yml -v

    PLAY [Testing] ************************************************************************************************

    TASK [Gathering Facts] ****************************************************************************************
    ok: [lpar22]

    TASK [Scan new devices.] **************************************************************************************
    changed: [lpar22] => {"changed": true, "failed": false, "msg": "", "state": "present"}

    TASK [Scan new virtual devices (vio0).] ***********************************************************************
    changed: [lpar22] => {"changed": true, "failed": false, "msg": "", "state": "present"}

    TASK [Removes ent2.] ******************************************************************************************
    changed: [lpar22] => {"changed": true, "failed": false, "msg": "ent2 deleted\n", "state": "absent"}

    TASK [Put device en2 in Defined] ******************************************************************************
    ok: [lpar22] => {"changed": false, "failed": false, "msg": "Device en2 already in Defined", "state": "defined"}

    TASK [Removes ent4 (inexistent).] *****************************************************************************
    ok: [lpar22] => {"changed": false, "failed": false, "msg": "Device ent4 does not exist.", "state": "absent"}

    TASK [Put device en4 in Defined (inexistent)] *****************************************************************
    ok: [lpar22] => {"changed": false, "failed": false, "msg": "Device en4 does not exist.", "state": "defined"}

    TASK [Put vscsi1 and children devices in Defined state.] ******************************************************
    changed: [lpar22] => {"changed": true, "failed": false, "msg": "vscsi1 Defined\n", "state": "defined"}

    TASK [Removes vscsi1 and children devices.] *******************************************************************
    changed: [lpar22] => {"changed": true, "failed": false, "msg": "vscsi1 deleted\n", "state": "absent"}

    TASK [Changes en1 mtu to 9000 and disables arp.] **************************************************************
    changed: [lpar22] => {"changed": true, "failed": false, "msg": "Attributes changed: arp=off. Attributes already set: mtu=900. ", "state": "present"}

    TASK [Configure IP, netmask and set en1 up.] ******************************************************************
    changed: [lpar22] => {"changed": true, "failed": false, "msg": "Attributes changed: netaddr=192.168.0.100,netmask=255.255.255.0,state=up. ", "state": "present"}

    TASK [Adding IP alias to en0] *********************************************************************************
    changed: [lpar22] => {"changed": true, "failed": false, "msg": "Attributes changed: alias4=10.0.0.100,255.255.255.0. ", "state": "present"}

    PLAY RECAP ****************************************************************************************************
    lpar22                     : ok=12   changed=8    unreachable=0    failed=0



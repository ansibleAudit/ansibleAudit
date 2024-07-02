import distro
from modules.run_playbooks import run_playbooks

# Roles directory path
roles_dir = 'roles'
run_playbooks(roles_dir)

# Setting up my client confg file
include stdlib

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
  match=> '^#?\s*IdentityFile',
}

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
  match=> '^#?\s*PasswordAuthentication',
}

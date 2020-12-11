# manifest set ssh_config file
file_line { 'No pass authorization':
  ensure =>  'present',
  path   =>  '/etc/ssh/ssh_config',
  line   =>  'PasswordAuthentication no',
}
file_line { 'set id file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton';
}

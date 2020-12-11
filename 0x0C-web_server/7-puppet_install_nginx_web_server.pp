# Install Nginx web server
exec { 'update apt-get':
  command => 'sudo apt-get update -y',
  path    => ['/usr/bin', '/bin'],
  returns =>[0, 1],
}

package { 'install nginx web server':
  ensure  => 'present',
  name    => 'nginx',
  require => Exec['update apt-get'],
}

exec { 'set content web server':
  command => 'echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html',
  path    => ['/usr/bin', '/bin'],
  returns =>[0, 1],
  require => Package['install nginx web server'],
}

exec { 'start nginx web server':
  command => 'sudo service nginx start',
  path    => ['/usr/bin', '/bin'],
  returns =>[0, 1],
  require => Exec['set content web server'],
}

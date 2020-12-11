# modify the limit of request
exec { 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 5000\"/g" /etc/default/nginx':
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec { 'service restart':
  command => '/usr/sbin/service nginx restart',
}

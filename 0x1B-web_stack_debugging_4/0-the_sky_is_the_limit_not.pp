#  Web debugging ULIMIT for nginx
exec { 'update ULIMIT--for-nginx':
  environment => ['DIR=/etc/default/nginx',
                  'OLD=ULIMIT="-n 15"',
                  'NEW=ULIMIT="-n 8192"'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR; sudo service nginx restart',
  path        => ['/usr/bin', '/bin'],
}

# open files fix
exec { 'fix--for-linux-secuity_limits':
  environment => ['DIR=/etc/security/limits.conf',
                  'OLD1=nofile 5',
                  'NEW1=nofile 15000',
                  'OLD2=nofile 4',
                  'NEW2=nofile 15000'],
  command     => 'sudo sed -i "s/$OLD1/$NEW1/" $DIR; sudo sed -i "s/$OLD2/$NEW2/" $DIR';
  path        => ['/usr/bin', '/bin'],
}

# Debug Apache server, typo in executable filename
exec { 'debuggin_3':
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
  command => 'sed -i "s/phpp/php/1" /var/www/html/wp-settings.php',
}


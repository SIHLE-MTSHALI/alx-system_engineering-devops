# Fix Apache 500 error by correcting wp-settings.php file permissions
exec { 'fix-wordpress':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}

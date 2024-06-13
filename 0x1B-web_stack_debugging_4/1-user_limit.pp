# This Puppet manifest is to increase the open file limit for the user holberton

exec { 'change-os-configuration-for-holberton-user':
  command => '/bin/echo "holberton soft nofile 65536\nholberton hard nofile 65536" >> /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
}

# Change OS configuration for holberton user
exec { 'change-os-configuration-for-holberton-user':
  command => 'sed -i "/holberton hard nofile/s/5/50000/" /etc/security/limits.conf;
              sed -i "/holberton soft nofile/s/4/40000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

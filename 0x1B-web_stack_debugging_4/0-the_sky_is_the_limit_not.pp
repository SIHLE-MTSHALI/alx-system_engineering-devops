# This Puppet manifest is to configure Nginx to handle more requests by tuning its settings

exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/worker_connections 768;/worker_connections 4096;/" /etc/nginx/nginx.conf && service nginx restart',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
}

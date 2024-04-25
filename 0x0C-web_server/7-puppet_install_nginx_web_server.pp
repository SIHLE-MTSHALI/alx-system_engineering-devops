package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file_line { 'Redirect 301 /redirect_me':
  path => '/etc/nginx/sites-available/default',
  line => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after => 'server_name _;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

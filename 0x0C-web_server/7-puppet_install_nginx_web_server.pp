class nginx_installation {
    package { 'nginx':
        ensure => present,
    }

    # Create a basic Nginx configuration with Hello World at the root
    file { '/var/www/html/index.html':
        ensure  => file,
        content => 'Hello World!',
    }

    # Create the redirection configuration
    file { '/etc/nginx/sites-available/redirect_config':
        ensure  => file,
        content => "
        server {
            listen 80;
            location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
            }
        }
        ",
    }

    # Enable the configuration
    file { '/etc/nginx/sites-enabled/redirect_config':
        ensure => link,
        target => '/etc/nginx/sites-available/redirect_config',
    }

    # Reload Nginx
    exec { 'nginx_reload':
        command => 'nginx -s reload',
        refreshonly => true,
        subscribe => File['/etc/nginx/sites-available/redirect_config'],
    }
}

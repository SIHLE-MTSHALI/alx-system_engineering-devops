# Using Puppet, install Flask from pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Ensure that pip3 is installed before installing Flask
package { 'python3-pip':
  ensure => 'present',
  before => Package['Flask'],
}

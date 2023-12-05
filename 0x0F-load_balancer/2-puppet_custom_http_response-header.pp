# Update package repositories using apt::update
include apt

apt::update { 'update':
  before => Package['nginx'],
}

# Install Nginx package
package { 'nginx':
  ensure  => 'latest',
  require => Apt::Update['update'],
}

# Configure Nginx with custom HTTP header
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "include /etc/nginx/sites-enabled/*;\n\tadd_header X-Served-By \"$hostname\";",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => Package['nginx'],
}

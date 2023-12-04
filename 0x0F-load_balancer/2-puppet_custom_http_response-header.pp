# Installs a Nginx server with custom HTTP header

# Update package repositories
exec { 'update':
  command => '/usr/bin/apt-get -y update',
  path    => ['/usr/bin'],
}

# Install Nginx package
package { 'nginx':
  ensure  => 'latest',
  require => Exec['update'],
}

# Configure Nginx with custom HTTP header
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "include /etc/nginx/sites-enabled/*;\n\tadd_header X-Served-By \"$hostname\";",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

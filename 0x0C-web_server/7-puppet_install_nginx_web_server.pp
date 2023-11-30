# Install nginx listening on port 80
# Get / returns a page that with content hello world

exec { 'install_nginx':
  command  => 'apt-get -y update; apt-get -y install nginx; ufw allow "Nginx HTTP"',
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

#file_line { 'redirect':
#  ensure => present,
#  path   => '/etc/nginx/sites-available/default',
#  after  => 'server_name _;',
#  line   => 'rewrite ^/redirect_me https://google.com permanent;',
#}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

# Fix request failures on high volume requests

exec { 'replace_ulimit':
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => 'sudo service nginx restart',
  refreshonly => true,
}


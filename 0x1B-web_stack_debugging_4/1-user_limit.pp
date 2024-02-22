# Fix open file without error.

exec { 'increase-nofile-limit':
  command     => 'sudo sed -i -e "s/nofile 5/nofile 50000/" -e "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  refreshonly => true,
  subscribe   => File['/etc/security/limits.conf'],
}

file { '/etc/security/limits.conf':
  ensure => present,
  notify => Exec['increase-nofile-limit'],
}


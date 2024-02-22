# Fix request failures on high volume requests

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
}


# Configure server to disallow password authentication

file_line { 'disable_password':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => "	PasswordAuthentication no",
  match   => '^\s*#?\s*PasswordAuthentication',
  replace => true,
}

file_line { 'identity':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => "	IdentityFile ~/.ssh/school",
  replace => true,
}


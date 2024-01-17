#Fix error with Apache returning 500

exec { 'Fix site':
     command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
     provider => shell,
}

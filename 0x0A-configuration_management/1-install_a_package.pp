# Install flask on pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.2.0',
  provider => 'pip3',
}

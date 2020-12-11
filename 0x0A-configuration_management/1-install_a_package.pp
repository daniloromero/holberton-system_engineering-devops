# install puppet-lint
package { 'install puppet-lint':
  ensure   => '2.1.1',
  provider => gem,
}


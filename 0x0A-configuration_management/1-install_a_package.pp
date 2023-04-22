#!/usr/bin/pup
# using puppet to install flask from pip3

file { 'flask':
provider => 'pip3',
ensure   => '2.1.0',
}

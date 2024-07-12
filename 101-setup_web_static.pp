# 101-setup_web_static.pp
node default {

  # Ensure the /data directory exists
  file { '/data':
    ensure => directory,
  }

  # Ensure the /data/web_static directory exists
  file { '/data/web_static':
    ensure => directory,
  }

  # Ensure the /data/web_static/releases directory exists
  file { '/data/web_static/releases':
    ensure => directory,
  }

  # Ensure the /data/web_static/shared directory exists
  file { '/data/web_static/shared':
    ensure => directory,
  }

  # Ensure the /data/web_static/releases/test directory exists
  file { '/data/web_static/releases/test':
    ensure => directory,
  }

  # Create the index.html file in the /data/web_static/releases/test directory
  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  }

  # Ensure the symbolic link /data/web_static/current points to /data/web_static/releases/test
  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
  }

  # Ensure the /data/web_static/releases/test directory and index.html file have appropriate permissions
  file { ['/data/web_static/releases/test', '/data/web_static/releases/test/index.html']:
    owner => 'root',
    group => 'root',
    mode  => '0755',
  }
}
apache-packages:
  pkg.installed:
    - pkgs:
        - apache2
        - libapache2-mod-wsgi-py3
        - python3-flask

trivia-app-files:
  file.recurse:
    - name: /var/www/trivia
    - source: salt://trivia/
    - user: www-data
    - group: www-data

trivia-apache-site:
  file.managed:
    - name: /etc/apache2/sites-available/trivia.conf
    - source: salt://trivia/apache/trivia.conf

enable-trivia-site:
  cmd.run:
    - name: a2ensite trivia.conf
    - unless: test -L /etc/apache2/sites-enabled/trivia.conf

disable-default-site:
  cmd.run:
    - name: a2dissite 000-default.conf

force-ipv4-port:
  file.replace:
    - name: /etc/apache2/ports.conf
    - pattern: '^Listen 80$'
    - repl: 'Listen 0.0.0.0:80'
    - backup: False

enable-wsgi-module-once:
  cmd.run:
    - name: a2enmod wsgi
    - unless: apache2ctl -M | grep -q wsgi

ensure-apache-running:
  service.running:
    - name: apache2
    - enable: True
    - watch:
        - cmd: enable-trivia-site
        - cmd: disable-default-site
        - file: trivia-apache-site

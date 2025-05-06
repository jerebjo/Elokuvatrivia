# Elokuvatrivia

Kahden tai useamman koneen elokuvatrivia-peli, joka asentuu automaattisesti Vagrantilla ja Saltilla.

![peliruutu](Kuvat/elokuvatrivia.png)

## Projektin tarkoitus

Elokuvatrivia on Flaskilla toteutettu monivalintapeli, joka toimii usean virtuaalikoneen välillä Saltin hallinnoimana. Jokainen pelaaja vastaa kysymyksiin omalta koneeltaan, ja pelin asennus onnistuu yhdellä komennolla.

## Tekijä

**Nimi:** Jere Björkstedt

**GitHub:** [jerebjo](https://github.com/jerebjo)

## Lisenssi

**GNU General Public License v3.0 (GPL-3.0)**  

[Lue lisenssi](LICENSE) 

## Lataus ja käyttöönotto


    $ git clone https://github.com/jerebjo/elokuvatrivia.git
    $ cd elokuvatrivia
    $ vagrant up

Tämän jälkeen kirjaudu master-koneelle: 

    $ vagrant ssh master

Koneen sisällä: 

    # Tarkista ja hyväksy avaimet
    $ sudo salt-key -L
    $ sudo salt-key -A
    # Aja init.sls tiedosto
    $ sudo salt '*' state.apply

### Pelaaminen

Avaa selaimessa: 

Pelaaja 1: http://192.168.88.102 

Pelaaja 2: http://192.168.88.103 

Pelaajat näkevät kysymykset selaimessaan ja voivat kilpailla toisiaan vastaan! 




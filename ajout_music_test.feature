@tag
Feature : nous allons faire decouvrir different musicien aux artistes de l atelier Verrochio


Scenario : Ecouter Jimi Hendrix
    Given une musique Jimi Hendrix
    When Splinter fait ecouter musique
    Then Jimi Hendrix est ecouter

Scenario Outline : ecouter musique
    Given musique <music>
    When Splinter fait ecouter musique
    Then musique <ajout_music>
    Examples:
      | music           | ajout_music              |
      | "Jimi Hendrix"  | "All along the watchtower "|
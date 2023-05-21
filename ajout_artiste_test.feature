
@tag
Feature : add les artistes pour devenir des surhumains qui combattent l'obscurentisme
    en tant que master Splinter,
    je veux que mes students deviennent des pointes en peinture, mais aussi en architecture, en sculture,
    en mathematics, etc...


Scenario : Ajout Leonardo
    Given un eleve Leonardo
    When Splinter accueil artiste
    Then Leonard est mon eleve

Scenario Outline : add artiste
    Given eleve <eleve>
    When Splinter accueil artiste
    Then artiste <ajouter_artiste>
    Examples:
      | eleve       | ajouter_artiste                   |
      | "Leonardo"  | "Bienvenu Leonardo a Verrochio"  |

#      | "Donatello" | "Bien venu Donatello a Verrochio" |
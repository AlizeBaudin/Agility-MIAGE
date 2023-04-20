
/**
 * Décrivez votre classe Splinter ici.
 *
 * @author (votre nom)
 * @version (un numéro de version ou une date)
 */
public class Splinter
{
    // variables d'instance - remplacez l'exemple qui suit par le vôtre
    private String nom;
    private int anneeNaissance;
    private Eleve maitreDe;
    private Verrochio atelier;
    /**
     * Constructeur d'objets de classe Splinter
     */
    public Splinter(String nom, int anneeNaissance) {
        this.nom = nom;
        this.anneeNaissance = anneeNaissance;
    }
    /**
     * getter and setter
    **/
    public String getNom() {
        return this.nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }


    /**
     * Fonction 
       **/
    public void prendreElev(Eleve artiste) {
        this.atelier.ajouterArtiste(artiste);
    }

    public void enCours() {
        this.maitreDe.apprentissage();
    }


}

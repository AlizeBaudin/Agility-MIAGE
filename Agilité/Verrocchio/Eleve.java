
public class Eleve
{
    // variables d'instance - remplacez l'exemple qui suit par le vôtre
    private String nom;
    private int anneeNaissance;
    private Verrochio atelier;
    private Splinter master;
    /**
     * Constructeur d'objets de classe Leonardo
     */
    public Eleve(String nom, int anneeNaissance,Verrochio atelier, Splinter master) {
        this.nom = nom;
        this.anneeNaissance = anneeNaissance;
        this.atelier = atelier;
        this.master = master;
    }

    public void dessiner() {
        System.out.println(this.nom + " dessine dans l'atelier " + this.atelier.getNom());
    }
    public void apprentissage() {
        System.out.println(this.nom +" apprend à dessiner dans l'atelier "+ this.atelier.getNom());
    }

}

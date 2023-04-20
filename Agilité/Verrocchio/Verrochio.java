import java.util.ArrayList;

public class Verrochio
{
    // variables d'instance 
    private String nom;
    private int dateFondation;
    private ArrayList<Eleve> artistes;

    /**
     * Constructeur d'objets de classe Verrochio
     */
    public Verrochio(String nom, int dateFondation,ArrayList<Eleve> artistes) {
        this.nom = nom;
        this.dateFondation = dateFondation;
        this.artistes = new ArrayList<Eleve>();
    
    }
    /** 
     * Getter et settrer 
    **/
    public String getNom() {
        return this.nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getDateFondation() {
        return this.dateFondation;
    }

    public void setDateFondation(int dateFondation) {
        this.dateFondation = dateFondation;
    }

    public ArrayList<Eleve> getArtistes() {
        return this.artistes;
    }

    public void setArtistes(ArrayList<Eleve> artistes) {
        this.artistes = artistes;
    }
    
/**
 * Fonction de la classe 
**/
    public void ajouterArtiste(Eleve nomArtiste) {
        this.artistes.add(nomArtiste);
    }
    public int nombreArtistes() {
        return this.artistes.size();
    }

    public void afficherArtistes() {
        System.out.println("Les artistes travaillant dans l'atelier sont : ");
        for (Eleve artiste : this.artistes) {
            System.out.println(artiste);
        }
    }

    public static void main(String[] args) {
        ArrayList<Eleve> artistes = new ArrayList<Eleve>();
        Verrochio atelier = new Verrochio("Verrochio", 1438, artistes);
        Splinter master = new Splinter("Splinter",1435);
        Eleve leonardo = new Eleve("Leonardo da Vinci", 1452 ,atelier, master);
        Eleve donatello = new Eleve("Donatello", 1452 ,atelier, master);
        Eleve raphaelo = new Eleve("Raphaelo", 1452 ,atelier, master);
        Eleve michelAngelo = new Eleve("Michel Angelo", 1452 ,atelier, master);
        atelier.ajouterArtiste(leonardo);
        atelier.ajouterArtiste(donatello);
        atelier.ajouterArtiste(raphaelo);
        atelier.ajouterArtiste(michelAngelo);
        System.out.println("L'atelier a " + atelier.nombreArtistes() + " artistes.");
        
        leonardo.dessiner();
        michelAngelo.apprentissage();
    }

}

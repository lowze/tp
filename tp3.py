// Lea H-2023 - �Caroline Houle et Yvon Charest

import java.util.HashSet;

class Categorie implements Comparable<Categorie>{
	private String nomCategorie;
	private HashSet<Invention>inventions;
	
	public Categorie(String categorie){
		nomCategorie = categorie;
		inventions = new HashSet<Invention>();		
	}
	
	public String getNomCategorie(){		
		return nomCategorie;
	}
	
	public HashSet<Invention> getInventions(){		
		return inventions;
	}
	
	public int compareTo (Categorie nomCategorieTemp){
		return nomCategorie.compareToIgnoreCase(nomCategorieTemp.getNomCategorie());		
	}
	
	public String toString(){
		return "toString de Categorie a completer";
	}	
}

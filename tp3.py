
import java.awt.Color;
import java.awt.EventQueue;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintStream;
import java.util.TreeSet;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.ScrollPaneConstants;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.border.TitledBorder;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Font;

// Lea H-2023 - ©Caroline Houle et Yvon Charest

public class InterfaceDemarrage {

	private JFrame frame;
	private JTextField txtCategoAjoutCatego;
	private JTextField txtCategoAjoutInv;
	private JTextField txtInventionAjoutInv;
	private JTextField txtInventeurAjoutInv;
	private JTextField txtAnneeAjoutInv;
	private JTextField txtInventionModif;
	private JTextField txtAnneeModif;
	private JTextField txtCategoSuppression;
	private JTextField txtInventeurAffInventions;
	private static JTextArea txtZoneAffichage; 

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					InterfaceDemarrage window = new InterfaceDemarrage();
					window.frame.setVisible(true);	
				
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
		
		//TreeSet<Categorie>arbreCategorie = new TreeSet<Categorie>();
		
	}

	/**
	 * Create the application.
	 */
	public InterfaceDemarrage() {
		initialize();
		redirigerLaConsole(); //permet de rediriger System.out dans le JTextArea
		System.out.println("Bienvenue! Commencez par ajouter une cat�gorie.");
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.getContentPane().setBackground(new Color(211, 211, 211));
		frame.setBounds(100, 100, 743, 457);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBackground(Color.LIGHT_GRAY);
		panel.setBorder(new TitledBorder(UIManager.getBorder("TitledBorder.border"), 
				"Ajouter une cat\u00E9gorie", 
				TitledBorder.LEADING, TitledBorder.TOP, null, Color.BLUE));
		panel.setBounds(6, 11, 344, 53);
		frame.getContentPane().add(panel);
		panel.setLayout(null);
		
		JLabel lblNomDeLa = new JLabel("Nom de la cat\u00E9gorie:");
		lblNomDeLa.setFont(new Font("Arial", Font.PLAIN, 10));
		lblNomDeLa.setHorizontalAlignment(SwingConstants.RIGHT);
		lblNomDeLa.setBounds(6, 20, 105, 26);
		panel.add(lblNomDeLa);
		
		txtCategoAjoutCatego = new JTextField();
		txtCategoAjoutCatego.setFont(new Font("Arial", Font.PLAIN, 11));
		txtCategoAjoutCatego.setBounds(126, 23, 105, 20);
		panel.add(txtCategoAjoutCatego);
		txtCategoAjoutCatego.setColumns(10);
		
		JButton btnAjouterCatego = new JButton("Ajouter");
		btnAjouterCatego.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				GestionInventions.ajouterCategorie(txtCategoAjoutCatego.getText().toLowerCase());
			}
		});
		btnAjouterCatego.setFont(new Font("Arial", Font.PLAIN, 10));
		btnAjouterCatego.setBounds(240, 22, 89, 23);
		panel.add(btnAjouterCatego);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBackground(Color.LIGHT_GRAY);
		panel_1.setBorder(new TitledBorder(UIManager.getBorder("TitledBorder.border"), 
				"Ajouter une invention", TitledBorder.LEADING, 
				TitledBorder.TOP, null, Color.BLUE));
		panel_1.setBounds(6, 70, 344, 147);
		frame.getContentPane().add(panel_1);
		panel_1.setLayout(null);
		
		JLabel lblCatgorie = new JLabel("Cat\u00E9gorie:");
		lblCatgorie.setFont(new Font("Arial", Font.PLAIN, 10));
		lblCatgorie.setBounds(6, 23, 110, 14);
		panel_1.add(lblCatgorie);
		lblCatgorie.setHorizontalAlignment(SwingConstants.RIGHT);
		
		txtCategoAjoutInv = new JTextField();
		txtCategoAjoutInv.setFont(new Font("Arial", Font.PLAIN, 11));
		txtCategoAjoutInv.setBounds(126, 20, 112, 20);
		panel_1.add(txtCategoAjoutInv);
		txtCategoAjoutInv.setColumns(10);
		
		JLabel lblNomDeLinvention = new JLabel("Nom de l'invention:");
		lblNomDeLinvention.setFont(new Font("Arial", Font.PLAIN, 10));
		lblNomDeLinvention.setBounds(6, 50, 110, 14);
		panel_1.add(lblNomDeLinvention);
		lblNomDeLinvention.setHorizontalAlignment(SwingConstants.RIGHT);
		
		txtInventionAjoutInv = new JTextField();
		txtInventionAjoutInv.setFont(new Font("Arial", Font.PLAIN, 11));
		txtInventionAjoutInv.setBounds(126, 51, 191, 20);
		panel_1.add(txtInventionAjoutInv);
		txtInventionAjoutInv.setColumns(10);
		
		JLabel lblNomDeLenventeur = new JLabel("Nom de l'inventeur:");
		lblNomDeLenventeur.setFont(new Font("Arial", Font.PLAIN, 10));
		lblNomDeLenventeur.setBounds(6, 78, 110, 14);
		panel_1.add(lblNomDeLenventeur);
		lblNomDeLenventeur.setHorizontalAlignment(SwingConstants.RIGHT);
		
		txtInventeurAjoutInv = new JTextField();
		txtInventeurAjoutInv.setFont(new Font("Arial", Font.PLAIN, 11));
		txtInventeurAjoutInv.setBounds(126, 75, 191, 20);
		panel_1.add(txtInventeurAjoutInv);
		txtInventeurAjoutInv.setColumns(10);
		
		JLabel lblAnneDeLinvention = new JLabel("Ann\u00E9e de l'invention:");
		lblAnneDeLinvention.setFont(new Font("Arial", Font.PLAIN, 10));
		lblAnneDeLinvention.setBounds(6, 106, 110, 14);
		panel_1.add(lblAnneDeLinvention);
		lblAnneDeLinvention.setHorizontalAlignment(SwingConstants.RIGHT);
		
		txtAnneeAjoutInv = new JTextField();
		txtAnneeAjoutInv.setFont(new Font("Arial", Font.PLAIN, 11));
		txtAnneeAjoutInv.setBounds(126, 103, 112, 20);
		panel_1.add(txtAnneeAjoutInv);
		txtAnneeAjoutInv.setColumns(10);
		
		JButton btnAjouterInvention = new JButton("Ajouter");
		btnAjouterInvention.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				GestionInventions.ajouterInvention(txtCategoAjoutInv.getText(),
						txtInventionAjoutInv.getText(), txtInventeurAjoutInv.getText(),
						Integer.parseInt(txtAnneeAjoutInv.getText()));
			}
		});
		btnAjouterInvention.setFont(new Font("Arial", Font.PLAIN, 10));
		btnAjouterInvention.setBounds(245, 102, 89, 23);
		panel_1.add(btnAjouterInvention);
		
		JPanel panel_2 = new JPanel();
		panel_2.setForeground(new Color(165, 42, 42));
		panel_2.setBackground(Color.LIGHT_GRAY);
		panel_2.setBorder(new TitledBorder(UIManager.getBorder("TitledBorder.border"),
				"Modifier l'ann\u00E9e d'une invention",
				TitledBorder.LEADING, TitledBorder.TOP, null, new Color(139, 0, 0)));
		panel_2.setBounds(360, 11, 357, 78);
		frame.getContentPane().add(panel_2);
		panel_2.setLayout(null);
		
		JLabel lblNomDeLinvention_1 = new JLabel("Nom de l'invention:");
		lblNomDeLinvention_1.setFont(new Font("Arial", Font.PLAIN, 10));
		lblNomDeLinvention_1.setBounds(16, 25, 97, 14);
		panel_2.add(lblNomDeLinvention_1);
		lblNomDeLinvention_1.setHorizontalAlignment(SwingConstants.RIGHT);
		
		txtInventionModif = new JTextField();
		txtInventionModif.setFont(new Font("Arial", Font.PLAIN, 11));
		txtInventionModif.setBounds(123, 22, 112, 20);
		panel_2.add(txtInventionModif);
		txtInventionModif.setColumns(10);
		
		JLabel lblNouvelleAnne = new JLabel("Nouvelle ann\u00E9e:");
		lblNouvelleAnne.setFont(new Font("Arial", Font.PLAIN, 10));
		lblNouvelleAnne.setBounds(16, 50, 97, 14);
		panel_2.add(lblNouvelleAnne);
		lblNouvelleAnne.setHorizontalAlignment(SwingConstants.RIGHT);
		
		txtAnneeModif = new JTextField();
		txtAnneeModif.setFont(new Font("Arial", Font.PLAIN, 11));
		txtAnneeModif.setBounds(123, 47, 112, 20);
		panel_2.add(txtAnneeModif);
		txtAnneeModif.setColumns(10);
		
		JButton btnModifierAnnee = new JButton("Modifier");
		btnModifierAnnee.setFont(new Font("Arial", Font.PLAIN, 10));
		btnModifierAnnee.setBounds(245, 46, 88, 23);
		panel_2.add(btnModifierAnnee);
		
		JPanel panel_3 = new JPanel();
		panel_3.setForeground(new Color(165, 42, 42));
		panel_3.setBackground(Color.LIGHT_GRAY);
		panel_3.setBorder(new TitledBorder(UIManager.getBorder("TitledBorder.border"),
				"Supprimer une cat\u00E9gorie", TitledBorder.LEADING,
				TitledBorder.TOP, null, new Color(139, 0, 0)));
		panel_3.setBounds(360, 95, 357, 50);
		frame.getContentPane().add(panel_3);
		panel_3.setLayout(null);
		
		JLabel label = new JLabel("Cat\u00E9gorie:");
		label.setFont(new Font("Arial", Font.PLAIN, 10));
		label.setBounds(6, 23, 110, 14);
		panel_3.add(label);
		label.setHorizontalAlignment(SwingConstants.RIGHT);
		
		txtCategoSuppression = new JTextField();
		txtCategoSuppression.setFont(new Font("Arial", Font.PLAIN, 11));
		txtCategoSuppression.setBounds(126, 20, 112, 20);
		panel_3.add(txtCategoSuppression);
		txtCategoSuppression.setColumns(10);
		
		JButton btnSupprimerCatego = new JButton("Supprimer");
		btnSupprimerCatego.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				GestionInventions.supprimerCategorie(txtCategoSuppression.getText());
			}
		});
		btnSupprimerCatego.setFont(new Font("Arial", Font.PLAIN, 10));
		btnSupprimerCatego.setBounds(248, 19, 89, 23);
		panel_3.add(btnSupprimerCatego);
		
		JPanel panel_4 = new JPanel();
		panel_4.setForeground(new Color(165, 42, 42));
		panel_4.setBackground(Color.LIGHT_GRAY);
		panel_4.setBorder(new TitledBorder(UIManager.getBorder("TitledBorder.border"),
				"Annuler la derni\u00E8re suppression", TitledBorder.LEADING,
				TitledBorder.TOP, null, new Color(139, 0, 0)));
		panel_4.setBounds(360, 156, 357, 61);
		frame.getContentPane().add(panel_4);
		panel_4.setLayout(null);
		
		JButton btnAnnulerDerniereSuppress = new JButton("Annuler la suppression la plus r\u00E9cente");
		btnAnnulerDerniereSuppress.setBounds(32, 27, 300, 23);
		panel_4.add(btnAnnulerDerniereSuppress);
		
		JButton btnAfficherCategories = new JButton("Afficher toutes les cat\u00E9gories et leurs inventions");
		btnAfficherCategories.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				GestionInventions.afficherCategories();
			}
		});
		btnAfficherCategories.setFont(new Font("Arial", Font.PLAIN, 11));
		btnAfficherCategories.setBounds(6, 228, 344, 50);
		frame.getContentPane().add(btnAfficherCategories);
		
		JPanel panel_5 = new JPanel();
		panel_5.setBackground(Color.LIGHT_GRAY);
		panel_5.setBorder(new TitledBorder(UIManager.getBorder("TitledBorder.border"),
				"Afficher les inventions d'un inventeur particulier", 
				TitledBorder.LEADING, TitledBorder.TOP, null, new Color(199, 21, 133)));
		panel_5.setBounds(360, 228, 357, 50);
		frame.getContentPane().add(panel_5);
		panel_5.setLayout(null);
		
		JLabel label_1 = new JLabel("Nom de l'inventeur:");
		label_1.setFont(new Font("Arial", Font.PLAIN, 10));
		label_1.setBounds(6, 24, 110, 14);
		panel_5.add(label_1);
		label_1.setHorizontalAlignment(SwingConstants.RIGHT);
		
		txtInventeurAffInventions = new JTextField();
		txtInventeurAffInventions.setFont(new Font("Arial", Font.PLAIN, 11));
		txtInventeurAffInventions.setBounds(126, 21, 112, 20);
		panel_5.add(txtInventeurAffInventions);
		txtInventeurAffInventions.setColumns(10);
		
		JButton btnAfficherInventionsDunInventeur = new JButton("Afficher");
		btnAfficherInventionsDunInventeur.setFont(new Font("Arial", Font.PLAIN, 10));
		btnAfficherInventionsDunInventeur.setBounds(248, 20, 89, 23);
		panel_5.add(btnAfficherInventionsDunInventeur);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
		scrollPane.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
		scrollPane.setBounds(6, 291, 711, 121);
		frame.getContentPane().add(scrollPane);
		
		txtZoneAffichage = new JTextArea();
		scrollPane.setViewportView(txtZoneAffichage);
		
		
	}
	
	/**
	 * 
	 * La m�thode qui suit permet la redirection de System.out vers le 
	 * JTextArea nomm� txtZoneAffichage
	 */

	private void redirigerLaConsole() { 
		OutputStream out = new OutputStream() { 
			@Override 
			public void write(int b) throws IOException { 
				txtZoneAffichage.append(String.valueOf((char) b)); 
			} 

			@Override 
			public void write(byte[] b, int off, int len) throws IOException { 
				txtZoneAffichage.append(new String(b, off, len)); 
			} 

			@Override 
			public void write(byte[] b) throws IOException { 
				write(b, 0, b.length); 
			} 
		}; 

		System.setOut(new PrintStream(out, true)); 
	}
}//fin classe

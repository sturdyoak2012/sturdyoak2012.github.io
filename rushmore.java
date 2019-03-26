/*Michelle Sheu
 * 2.25.19
 * MountRushmore.java*/
import java.awt.*;   // for classes Graphics, Color, Font, Image
import java.util.Scanner;
import java.awt.event.* ; // for classes KeyListener, MouseListener
 
import javax.swing.* ; // for classes JFrame, JPanel, JLabel
 
import java.*  ; // for classes File, IOException, ImageIO
public class MountRushmore extends JFrame
{
 public MountRushmore ( )  
 {
    super ("MountRushmore");
    setSize( 600, 600);    
    setDefaultCloseOperation(DISPOSE_ON_CLOSE);  
    setLocation(200,100);
    setResizable(true);
    Panel pan = new Panel();  
    setContentPane(pan);  
    setVisible(true);
   
 }
 
 public static void main (String[] args)
 {
  MountRushmore mr = new MountRushmore();
 }
}
 
class Panel extends JPanel
{  
  public Panel()
  {  
  }
  public void paintComponent(Graphics g)
  {  
      super.paintComponent(g);
    Image rush = new ImageIcon("zz_mountrushmore.jpg").getImage();    
    g.drawImage(rush, 0, 0, 600, 600, null);    
    Image adams = new ImageIcon("adams.jpg").getImage();
    g.drawImage(adams,40,80,160,160,null);
    Image hoov = new ImageIcon("hoover.jpg").getImage();
    Image ike = new ImageIcon("ike.jpg").getImage();
    Image quinc = new ImageIcon("quincyadams.jpg").getImage();
    g.drawImage(hoov,200,160,140,160,null);
    g.drawImage(ike,320,240,120,160,null);
    g.drawImage(quinc,440,200,160,200,null);
   
   for(int i = 0; i<600;i+=40)
    {
     g.setColor(Color.BLACK);    //lines will be black
     g.drawLine(i, 0, i, 600);   //draws vertical lines
     g.drawLine(0, i, 600, i);   //draws horizontal lines
    }
    //if (evt.iskeyPressed())
    {
    Scanner kb = new Scanner(System.in);
    System.out.println("\n\n\nMy presidents are Adams(1), Hoover(2), Ike(3), Quincy Adams(4). Which order would you like?");
     
   
    int pic1,pic2,pic3,pic4;
    pic1 =kb.nextInt();
    pic2 =kb.nextInt();    
    pic3=kb.nextInt();
    pic4 =kb.nextInt();
 
 
    Image adamsN = new ImageIcon("adams.png").getImage();
    Image hoovN = new ImageIcon("hoover.png").getImage();
    Image ikeN = new ImageIcon("ike.png").getImage();
    Image quincN = new ImageIcon("quincyadams.png").getImage();    
    g.drawImage(rush, 0, 0, 600, 600, null);    
 
    if(pic1==1)
      g.drawImage(adamsN,40,80,160,160,null);
    else if(pic1==2)
      g.drawImage(hoovN,40,80,160,160,null);
    else if(pic1==3)
      g.drawImage(ikeN,40,80,160,160,null);
    else
      g.drawImage(quincN,40,80,160,160,null);
    if(pic2==1)
      g.drawImage(adamsN,200,160,140,160,null);
    else if(pic2==2)
      g.drawImage(hoovN,200,160,140,160,null);
    else if(pic2==3)
      g.drawImage(ikeN,200,160,140,160,null);
    else
      g.drawImage(quincN,200,160,140,160,null);
    if(pic3==1)
      g.drawImage(adamsN,320,240,120,160,null);
    else if(pic3==2)
      g.drawImage(hoovN,320,240,120,160,null);
    else if(pic3==3)
      g.drawImage(ikeN,320,240,120,160,null);
    else
      g.drawImage(quincN,320,240,120,160,null);
    if(pic4==1)
      g.drawImage(adamsN,440,200,160,200,null);
    else if(pic4==2)
      g.drawImage(hoovN,440,200,160,200,null);
    else if(pic4==3)
      g.drawImage(ikeN,440,200,160,200,null);
    else
      g.drawImage(quincN,440,200,160,200,null);
 
    System.out.println("Thank you. Here is YOUR Mount Rushmore\n\n\n");
  }
}
}
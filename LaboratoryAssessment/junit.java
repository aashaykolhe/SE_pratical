
/* 

Author: Alia Ibrahim Bandarkar



*/
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import javax.mail.*;
import javax.mail.internet.*;


public class Mail_OTP {

    static int num_of_characters = 3;
    static int num_of_numbers = 3;
    static int length;
    static String sender_mail = "";
    static String Password = "";
    static Scanner s = new Scanner(System.in);
    static String  receiver_mail ;
    static int tries;
    // Function to generate a One Time Password
    static String generate_otp() {
        length = num_of_characters + num_of_numbers;
        Random random = new Random();
        String number = "0123456789";
     
        String otp = "";
//        ShuffleString x = new ShuffleString();
        for (int i = 0; i < length; i++) {
            int index;
            
                index = random.nextInt(9);
                otp += number.charAt(index);
                

        }
        return otp;
    }

    // Function to configure parameters for the program
   
    static void setSender_mail(){
        System.out.println("Enter sender's e-mail address");
        String sender = s.nextLine();
        sender_mail = sender;
        System.out.println("Sender's email has been changed successfully!\n Set up password");
    }
    
    public static void send_mail(final String sender_mail,final String password,final String receiver_mail,String sub,String msg){
        //Get properties object
        Properties props = new Properties();
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.host", "smtp.gmail.com");
        props.put("mail.smtp.socketFactory.port", "587");
        props.put("mail.smtp.socketFactory.class",
                "javax.net.ssl.SSLSocketFactory");
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.port", "587");
        props.put("mail.smtp.ssl.protocols", "TLSv1.2");
        //get Session
        Session session = Session.getDefaultInstance(props,
                new javax.mail.Authenticator() {
                    protected PasswordAuthentication getPasswordAuthentication() {
                        return new PasswordAuthentication(sender_mail,password);
                    }
                });
        //compose message
        try {
            MimeMessage message = new MimeMessage(session);
            message.addRecipient(Message.RecipientType.TO,new InternetAddress(receiver_mail));
            message.setSubject(sub);
            message.setText(msg);
            //send message
            Transport.send(message);
            System.out.println("message sent successfully");
        } catch (MessagingException e) {throw new RuntimeException(e);}

    }

    static boolean verify_otp(String otp, String user_otp){
        if(Objects.equals(user_otp, otp))  return true; 
        else return false;
    }

    // main function
    public static void main(String[] args) {
    	
    	boolean run_program = true;
    	
    	while(run_program) {
    		System.out.println("Press \n 1 Send OTP\n 2 Exit");
    		int choice = s.nextInt();
    		s.nextLine();
    		if (choice == 1) {
        	
        	 // Generate OTP
        	 String otp = generate_otp();
        	 
        	 // Append OTP to message
             String message = "This your OTP: "+ otp;
             String subject = "OTP";
             
             // Take input for receiver's mail address 
             System.out.println("Enter receiver's e-mail address: ");
             receiver_mail = s.nextLine();
             
             // Send email to the receiver 
             send_mail(sender_mail, Password,receiver_mail,subject,message);
             System.out.println("OTP sent successfully to "+ receiver_mail);
             
             // Take input of user for OTP
             String user_otp;
             System.out.println("Enter the sent otp: ");
//             s.nextLine();
             user_otp = s.nextLine();
             
             boolean try_again = true;
             tries = 0 ;
             while(try_again) {
            	 tries++;
             if(verify_otp(otp,user_otp))
             {System.out.println("OTP verified"); try_again  = false;}
             else if(tries>2) {
            	 System.out.println("You have reached the limit!");
            	 break;
             }
             else {
            	 System.out.println("The entered OTP was incorrect! Please Try again\nEnter OTP or press 0 to resend OTP ");
                 user_otp = s.nextLine();
                 if(user_otp == "0") {try_again = false; main(null);}
             }
             }
             
         }
        else if (choice == 2) break;
       }
    	}
    }

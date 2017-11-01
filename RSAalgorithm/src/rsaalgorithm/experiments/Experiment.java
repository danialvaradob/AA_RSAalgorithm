/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rsaalgorithm.experiments;

import java.io.IOException;
import java.security.KeyFactory;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.RSAPrivateKeySpec;
import java.security.spec.RSAPublicKeySpec;
import rsaalgorithm.*;

/**
 *
 * @author danielalvarado
 */
public class Experiment {
    
    
    public int loops;
    public String message;
    public long totalTime;
    public long avgTime;
    private static final String PUBLIC_KEY_FILE = "Public.key";
    private static final String PRIVATE_KEY_FILE = "Private.key";
    
    
    public Experiment(int l, String _message) throws IOException {
        loops = l;
        message = _message;
        run();
    }
    
    
    public void run() throws IOException {

		try {
                        //DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
                        //Date date = new Date();
                        //System.out.println(dateFormat.format(date)); 
                        
                        //System.out.println(millis);
			System.out.println("-------GENRATE PUBLIC and PRIVATE KEY-------------");
			KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
			keyPairGenerator.initialize(2048); //1024 used for normal securitie
			KeyPair keyPair = keyPairGenerator.generateKeyPair();
			PublicKey publicKey = keyPair.getPublic();
			PrivateKey privateKey = keyPair.getPrivate();
			System.out.println("Public Key - " + publicKey);
			System.out.println("Private Key - " + privateKey);

			//Pullingout parameters which makes up Key
			System.out.println("\n------- PULLING OUT PARAMETERS WHICH MAKES KEYPAIR----------\n");
			KeyFactory keyFactory = KeyFactory.getInstance("RSA");
			RSAPublicKeySpec rsaPubKeySpec = keyFactory.getKeySpec(publicKey, RSAPublicKeySpec.class);
			RSAPrivateKeySpec rsaPrivKeySpec = keyFactory.getKeySpec(privateKey, RSAPrivateKeySpec.class);
			System.out.println("PubKey Modulus : " + rsaPubKeySpec.getModulus());
			System.out.println("PubKey Exponent : " + rsaPubKeySpec.getPublicExponent());
			System.out.println("PrivKey Modulus : " + rsaPrivKeySpec.getModulus());
			System.out.println("PrivKey Exponent : " + rsaPrivKeySpec.getPrivateExponent());
			
			//Share public key with other so they can encrypt data and decrypt thoses using private key(Don't share with Other)
			System.out.println("\n--------SAVING PUBLIC KEY AND PRIVATE KEY TO FILES-------\n");
			RSAalgorithm rsaObj = new RSAalgorithm();
			rsaObj.saveKeys(PUBLIC_KEY_FILE, rsaPubKeySpec.getModulus(), rsaPubKeySpec.getPublicExponent());
			rsaObj.saveKeys(PRIVATE_KEY_FILE, rsaPrivKeySpec.getModulus(), rsaPrivKeySpec.getPrivateExponent());
			
			//Encrypt Data using Public Key
			for (int times = 0;times <= this.loops;times++) {
                            long millis = System.nanoTime();
                            byte[] encryptedData = rsaObj.encryptData(this.message);
                            rsaObj.decryptData(encryptedData);
                            long millis2 = System.nanoTime();
                            long m = millis2 - millis;
                            this.totalTime += m;
                        }
                        this.avgTime = this.totalTime/this.loops;
                        
			
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}catch (InvalidKeySpecException e) {
			e.printStackTrace();
		}

	}
    
    
}

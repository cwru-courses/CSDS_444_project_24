package application;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.ByteArrayOutputStream;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
import java.lang.*;

public class MD5Picture {
	private static final int A = (int) 0x67452301;
    private static final int B = (int) 0xEFCDAB89L;
    private static final int C = (int) 0x98BADCFEL;
    private static final int D = (int) 0x10325476;

    private final static int K[]={
        0xd76aa478,0xe8c7b756,0x242070db,0xc1bdceee,
        0xf57c0faf,0x4787c62a,0xa8304613,0xfd469501,0x698098d8,
        0x8b44f7af,0xffff5bb1,0x895cd7be,0x6b901122,0xfd987193,
        0xa679438e,0x49b40821,0xf61e2562,0xc040b340,0x265e5a51,
        0xe9b6c7aa,0xd62f105d,0x02441453,0xd8a1e681,0xe7d3fbc8,
        0x21e1cde6,0xc33707d6,0xf4d50d87,0x455a14ed,0xa9e3e905,
        0xfcefa3f8,0x676f02d9,0x8d2a4c8a,0xfffa3942,0x8771f681,
        0x6d9d6122,0xfde5380c,0xa4beea44,0x4bdecfa9,0xf6bb4b60,
        0xbebfbc70,0x289b7ec6,0xeaa127fa,0xd4ef3085,0x04881d05,
        0xd9d4d039,0xe6db99e5,0x1fa27cf8,0xc4ac5665,0xf4292244,
        0x432aff97,0xab9423a7,0xfc93a039,0x655b59c3,0x8f0ccc92,
        0xffeff47d,0x85845dd1,0x6fa87e4f,0xfe2ce6e0,0xa3014314,
        0x4e0811a1,0xf7537e82,0xbd3af235,0x2ad7d2bb,0xeb86d391};
    
    private final static int s[]={7,12,17,22,7,12,17,22,7,12,17,22,7,
        12,17,22,5,9,14,20,5,9,14,20,5,9,14,20,5,9,14,20,
        4,11,16,23,4,11,16,23,4,11,16,23,4,11,16,23,6,10,
        15,21,6,10,15,21,6,10,15,21,6,10,15,21};

    public static String computeMD5(byte[] messageInByte) {
    	// Initialize value
    	int Atemp = A;
    	int Btemp = B;
    	int Ctemp = C;
    	int Dtemp = D;
    	
    	
    	int[] strByte = paddingBytes(messageInByte);
    	for (int i = 0; i < strByte.length/16; i++) {
    		// make a copy of the data to be processed for use
    		int[] processing = new int[16];
    		for (int j = 0; j < 16; j ++) {
    			processing[j] = strByte[i * 16 + j];
    		}
    		int F, g;
    		int a = Atemp;
    		int b = Btemp;
    		int c = Ctemp;
    		int d = Dtemp;
    		for (int j = 0; j < 64; j++) {
    			if (j < 16) {
    				F = (b & c) | ((~b) & d);
    				g = j;
    			}
    			else if (j < 32) {
    				F = (d & b) | ((~d) & c);
                    g=(5 * j + 1) % 16;
    			}
    			else if (j < 48) {
    				F = b ^ c ^ d;
    				g = (3 * j + 5) % 16;
    			}
    			else {
    				F = c ^ (b | (~d));
    				g = (7 * j) % 16;
    			}
    			int temp = d;
    			d = c;
    			c = b;
    			b = b + (((a + F + K[j] + 
    					processing[g]) << 
    					s[j]) | 
    					(a + F + K[j] + processing[g]) >>> (32 - s[j]));
    			a = temp;
    		}
        	Atemp = a + Atemp;
        	Btemp = b + Btemp;
        	Ctemp = c + Ctemp;
        	Dtemp = d + Dtemp;
    	}


    	return intToHaxString(Atemp) + 
    			intToHaxString(Btemp) + 
    			intToHaxString(Ctemp) + 
    			intToHaxString(Dtemp);
    }
    
    private static int[] paddingBytes(byte[] strInByte) {
    	int length = ((strInByte.length + 8) / 64) + 1;
    	int[] strByteInInt = new int[length*16];
    	for (int i = 0; i < strByteInInt.length; i++) {
    		strByteInInt[i] = 0;
    	}
    	
    	int i;
    	// add original string into the array
    	 for (i = 0; i < strInByte.length; i++) {
 	    	strByteInInt[i/4] = strByteInInt[i/4] << 8;
 	    	strByteInInt[i/4] |= strInByte[i];
 	    }
    	// add additional 1
    	strByteInInt[i>>2] |= 0x80 << ((i % 4) *8);
    	
    	// add length at the end
    	strByteInInt[length*16-2] = strInByte.length*8;
    	
    	return strByteInInt;
    }
    
    private static String intToHaxString(int num) {
    	StringBuilder builder = new StringBuilder();
    	for (int i = 0; i < 4; i++) {
    		builder.append(String.format("%2s", Integer.toHexString(((num >> i * 8) % (1 << 8)) & 0xff)).replace(' ', '0'));
    	}
    	return builder.toString();
    }
    
    
	public static String PictureMD5(File file) {
		File outputFile = new File("encryptedPicture.txt");
		String result = "";
		try {
			long startTime = System.currentTimeMillis();
			outputFile.createNewFile();
			FileWriter writer;
			writer = new FileWriter("encryptedPicture.txt");
			String extension = "";
			int i = file.getName().lastIndexOf('.');
			if (i > 0) {
			    extension = file.getName().substring(i+1);
			}
			BufferedImage bImage = ImageIO.read(file);
		    ByteArrayOutputStream bos = new ByteArrayOutputStream();
		    ImageIO.write(bImage, extension, bos );
		    byte [] data = bos.toByteArray();
		    result = computeMD5(data);
		    writer.write(result);
		    long timeSpent = System.currentTimeMillis() - startTime;
		    writer.append('\r');
		    writer.write("time spent for enciphering: " + timeSpent/1000 + "s");
			writer.close();
			System.out.println("enciphering finished");
		} catch (IOException e) {
			e.printStackTrace();
		}
		return result;
	}

}

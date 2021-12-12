package application;
	
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import javafx.geometry.*;
import javafx.scene.paint.*;
import javafx.scene.canvas.*;
import javafx.scene.text.*;
import javafx.scene.Group;
import javafx.scene.shape.*;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.collections.*;
import java.io.*;
import java.util.Objects;

import javax.swing.JTextArea;

import javafx.stage.FileChooser;


public class Main extends Application {
	
	public String messageOutput;
	
	@Override
	public void start(Stage stage) {
		try {
			FileChooser fileChooser = new FileChooser();

	        Button button = new Button("Select File");
	        TextArea text = new TextArea();
	        // button event handler
	        EventHandler<ActionEvent> event = new EventHandler<ActionEvent>() {
	            public void handle(ActionEvent e)
	            {
	            	text.setText("now calculating...");
	            	File selectedFile = fileChooser.showOpenDialog(stage);
	            	messageOutput = calculateMD5(selectedFile);
	                text.setText(messageOutput);
	            }
	        };
	        
	        button.setOnAction(event);
	        
			
			text.setEditable(false);
	        VBox vBox = new VBox(button, text);
	        Scene scene = new Scene(vBox, 960, 600);

	        stage.setScene(scene);
	        stage.setTitle("MD5 Encipher");
	        stage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	private static String calculateMD5(File file) {
		String filePath = "";
		if (Objects.nonNull(file))
			filePath = file.getPath();
		String extension = "";
		int i = filePath.lastIndexOf('.');
		if (i > 0) {
		    extension = filePath.substring(i+1);
		}
		StringBuilder encipheredMessage = new StringBuilder("file type not available. Only txt, jpg, or png file available right now");
		long startTime = System.currentTimeMillis();
		if (extension.equals("txt"))
			encipheredMessage = new StringBuilder(MD5.txtMD5(filePath));
		else if (extension.equals("jpg") || extension.equals("png"))
			encipheredMessage = new StringBuilder(MD5Picture.PictureMD5(file));
		long timeSpent = (System.currentTimeMillis() - startTime);
		if (timeSpent <= 10000)
			encipheredMessage.append("\r\n" + "time spent for enciphering is " + timeSpent + " ms.");
		else 
			encipheredMessage.append("\r\n" + "time spent for enciphering is " + timeSpent/1000 + " seconds.");
		return encipheredMessage.toString();
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}

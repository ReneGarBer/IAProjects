import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class LectorCSV {
    private char delimiter;
    private char escape;
    private char eol;
    private char quotes;

    public LectorCSV(){
        this.delimiter = ',';
        this.escape='\\';
        this.eol='\n';
        this.quotes ='\"';
    }

    public LectorCSV(char delimiter,char escape, char eol, char quotes){
        this.delimiter = delimiter;
        this.escape = escape;
        this.eol = eol;
        this.quotes = quotes;
    }

    public char getDelimiter() {
        return delimiter;
    }

    public void setDelimiter(char delimiter) {
        this.delimiter = delimiter;
    }

    public char getEscape() {
        return escape;
    }

    public void setEscape(char escape) {
        this.escape = escape;
    }

    public char getEol() {
        return eol;
    }

    public void setEol(char eol) {
        this.eol = eol;
    }

    public char getQuotes() {
        return quotes;
    }

    public void setQuotes(char quotes) {
        this.quotes = quotes;
    }
    
    public static ArrayList<String[]> csvToStringArray(String path,char delimiter){
        ArrayList<String[]> data = new ArrayList<>();
        String line = "";
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            while ((line = br.readLine()) != null) {
                String[] values = line.split(""+delimiter);
                data.add(values);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return data;
    }

    public ArrayList<String[]> csvToStringArray(String path){
        ArrayList<String[]> data = new ArrayList<>();
        String line = "";
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            while ((line = br.readLine()) != null) {
                String[] values = line.split(""+this.delimiter);
                data.add(values);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return data;
    }
}

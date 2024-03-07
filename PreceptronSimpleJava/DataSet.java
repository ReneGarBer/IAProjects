//divide los datos en particiones
//Altera valores
//Elimina valores
//ordena valores
//Los manda a archivo csv
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class DataSet {
    
    private ArrayList<String[]> dataset;
    private boolean[] partition;
    private int size;
    private String[] headers;
    private int dimentions;
    private int label_column;
    private int[] l_count;

    public int getLabel_column() {
        return label_column;
    }

    public int getDimentions() {
        return dimentions;
    }

    public DataSet(){
        this.dataset = new ArrayList<>();
        this.label_column = -1;
        this.l_count = new int[2];
    }

    public DataSet(DataSet dataset, int label_column){
        this.setDataset(dataset.dataset,label_column);
        this.l_count = new int[2];
        count();
    }

    public void setDataset(ArrayList<String[]> dataset,int label_column) {
        this.dataset = dataset;
        this.size = dataset.size();
        this.partition = new boolean[this.size];
        this.dimentions = dataset.get(1).length;
        this.label_column = label_column;
        count();
    }

    public String[] getHeaders() {
        return headers;
    }

    public int size() {
        return size;
    }

    public void setHeaders(String[] headers) {
        this.headers = headers;
    }
    
    public void setDataFromCSV(String path,int label_column){
        this.dataset = LectorCSV.csvToStringArray(path, ',');
        this.size = this.dataset.size();
        this.partition = new boolean[this.size];
        this.dimentions = this.dataset.get(0).length;
        if(label_column!=-1){
            this.dimentions--;
            this.label_column = label_column;
        }
        count();
    }
    
    public String[] getRow(int i){
        return this.dataset.get(i);
    }

    public float[] getRowNumeric(int i){
        float[] row = new float[this.dimentions];
        for(int j = 0; j < this.dimentions; j++){
            row[j] = this.getColumnFloat(i, j);
        } 
        return row;
    }

    public String getColumnStr(int i,int j){
        return this.dataset.get(i)[j];
    }

    public float getColumnFloat(int i,int j){
        float column = Float.NEGATIVE_INFINITY;
        try {
            column = Float.parseFloat(this.dataset.get(i)[j]);
            //System.out.println("Float value: " + column);
        } catch (NumberFormatException e) {
            //System.out.println("Invalid input: " + Float.parseFloat(this.dataset.get(i)[j]));
        }
        return column;
    }

    public String rowToStr(int i){
        String row="";

        for(String column: this.dataset.get(i)){
            row += column+",";
        }
        row = row.substring(0, row.length()-1);
        return row;
    }

    public void head(int i){
        try {
            for(int j = 0; j < i; j++){
                System.out.println(this.dataset.get(j).toString());
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public void tail(int i){
        try {
            for(int j = this.dataset.size()-i; j < this.dataset.size(); j++){
                System.out.println(this.dataset.get(j).toString());
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public void print(){
        if(this.headers != null){
            for(int i = 0; i < this.headers.length-1; i++){
                System.out.print(this.headers[i]+", ");
            }
            System.out.println(this.headers[this.headers.length-1]);
        }
        int k = 0;
        for(String[] row: this.dataset){
            System.out.print(k+": ");
            for(int i = 0; i < row.length-1; i++){
                System.out.print(row[i]+", ");
            }
            System.out.println(row[this.headers.length-1]);
            k++;
        }
    }

    public void divideDataSet(int mode){
        erasePartition();
        int count = (int)(this.size * 0.2);
        int i;
        Random rand;
        switch (mode) {
            case 1:
                rand = new Random();               
                while(count>0){
                    i = rand.nextInt(this.size);
                    if(!this.partition[i]){
                        this.partition[i]=true;
                        count--;
                    }
                }
                break;
            case 2:
                while(count > 0){
                    this.partition[this.partition.length-count]= true;
                    count--;
                }
                break;
            case 3:
                i = 0;
                while(count>0&&i<this.size){
                    if(this.dataset.get(i)[3].equals("-1")){
                        this.partition[i]= true;
                        count--;
                    }
                    i++;
                }
                break;
            case 4:
                i = 0;
                while(count>0&&i<this.size){
                    if(this.dataset.get(i)[3].equals("1")){
                        this.partition[i]= true;
                        count--;
                    }
                    i++;
                }
                break;
            case 5:
                int tp=0;
                for(i = 0; i < this.size; i++){
                    if(this.dataset.get(i)[3].equals("1")){
                        tp++;
                    }
                }
                float prc = (float)(tp/(float)this.size) ;
                rand = new Random(); 
                count = (int)(200 * prc); 
                while(count>0){
                    i = rand.nextInt(this.size);
                    if(this.dataset.get(i)[3].equals("1")){
                        this.partition[i]=true;
                        count--;
                    }
                }
                count = (int)(200 * prc);
                while(count<200){
                    i = rand.nextInt(this.size);
                    if(this.dataset.get(i)[3].equals("-1")){
                        this.partition[i]=true;
                        count++;
                    }
                }
                break;
            default:
                break;
        }
    }

    public DataSet getTestDataSet(){
        ArrayList<String[]> data = new ArrayList<>();
        for(int i = 0; i < this.size; i++){
            if(partition[i])
                data.add(this.dataset.get(i));
        }

        DataSet test = new DataSet();
        test.setDataset(data,this.label_column);
        return test;
    }

    public DataSet getTrainingtDataSet(){
        ArrayList<String[]> data = new ArrayList<>();
        for(int i = 0; i < this.size; i++){
            if(!partition[i])
                data.add(this.dataset.get(i));
        }

        DataSet test = new DataSet();
        test.setDataset(data,this.label_column);
        return test;
    }

    public void erasePartition(){
        Arrays.fill(this.partition,false);
    }

    public void printTraining(){
        if(this.headers != null){
            for(int i = 0; i < this.headers.length-1; i++){
                System.out.print(this.headers[i]+", ");
            }
            System.out.println(this.headers[this.headers.length-1]);
        }
        int j = 0;
        for(String[] row: this.dataset){
            if(!this.partition[j]){
                System.out.print(j+": ");
                for(int i = 0; i < row.length-1; i++){
                    System.out.print(row[i]+", ");
                }
                System.out.println(row[this.headers.length-1]);
            }
            j++;
        }
    }

    public void printTest(){
        if(this.headers != null){
            for(int i = 0; i < this.headers.length-1; i++){
                System.out.print(this.headers[i]+", ");
            }
            System.out.println(this.headers[this.headers.length-1]);
        }
        int j = 0;
        for(String[] row: this.dataset){
            if(this.partition[j]){
                System.out.print(j+": ");
                for(int i = 0; i < row.length-1; i++){
                    System.out.print(row[i]+", ");
                }
                System.out.println(row[this.headers.length-1]);
            }
            j++;
        }
    }

    private void count(){
        for(String[] row: dataset){
            int j = row[this.label_column].equals("1")? 1:0;
            this.l_count[j]++;            
        }
    }

    public int getPositivos(){
        return this.l_count[1];
    }

    public int getNegativos(){
        return this.l_count[0];
    }
}

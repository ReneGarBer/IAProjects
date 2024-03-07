import java.util.Random;

public class PerceptronSimple {
    private DataSet dataset;
    private int[] fpn;
    private int[] vpn;
    private float precision;
    private int epocas;
    private float[] w;
    private float l_rate;
    private float sesgo;

    public PerceptronSimple(DataSet dataset,  float l_rate, int epocas) {
        this.dataset = dataset;
        this.epocas = epocas;
        this.l_rate = l_rate;
        this.precision = 0;
        this.fpn = new int[2];
        this.vpn = new int[2];
    }

    public PerceptronSimple(DataSet dataset) {
        this.dataset = dataset;
    }

    public void entrenar(DataSet dataset,float precision){
        this.iniciarPesos();
        int lc = dataset.getLabel_column();
        int i = 0;
        
        while(this.precision < precision && i < this.epocas){
        //while(this.precision < precision){

            int hit = 0;
            for(int j = 0; j < dataset.size();j++){
                float[] x = dataset.getRowNumeric(j);
                int p = this.predecir(x);
                int p1 = p==0?-1:1;
                if((int)x[lc] != p1){
                    modifiedW(x, (int)x[lc], p);
                }else{
                    hit++;
                }
            }
            this.precision = hit/(float)dataset.size();
            i++;
        }
    }

    public void probar(DataSet dataset){
        this.restartMetrics();
        for(int i = 0; i < dataset.size(); i++){
            int result = predecir(dataset.getRowNumeric(i));
            this.printPrediction(dataset.getRow(i), result);
            int label = dataset.getRowNumeric(i)[dataset.getLabel_column()] < 0? 0 : 1;
            if(result != label){
                this.fpn[result]++;
            }else{
                this.vpn[result]++;
            }
        }
    }

    public int predecir(float[] x){
        float suma = Formulas.dot(x, this.w) + this.sesgo;
        return activacion(suma);
    }

    private void iniciarPesos(){
        Random rand = new Random();
        this.w = new float[this.dataset.getDimentions()];
        this.sesgo = rand.nextFloat()*0.1f;
        //this.sesgo = 0.1f;      
        for(int j = 0; j < this.dataset.getDimentions(); j++){
            w[j] = rand.nextFloat();
        }
    }

    private int activacion(float entrada){
        return entrada >=0? 1:0;
    }

    public void setEpocas(int epocas) {
        this.epocas = epocas;
    }

    public void setPrecision(float precision) {
        this.precision = precision;
    }

    public void setL_rate(float l_rate) {
        this.l_rate = l_rate;
    }

    private void modifiedW(float[] x,int l,int p){
        for(int i = 0; i < w.length; i++){
            this.w[i] = w[i] + this.l_rate*(l-p)*x[i];
        }
    }

    private void printPrediction(String[] row, int result){
        result = result == 0? -1:1;
        for(int i = 0; i < row.length-2; i++){
            System.out.print(row[i]+", ");
        }

        System.out.print("Valor real: "+row[row.length-1]+". Prediccion: "+result+"\n");
    }

    private void restartMetrics(){
        this.fpn[0] = 0;
        this.fpn[1] = 0;
        this.vpn[0] = 0;
        this.vpn[1] = 0;
    }

    public void printmatriz(){
        System.out.println("Verdaderos Positivos: "+this.vpn[1]+" Verdaderos Negativos: "+this.vpn[0]);
        System.out.println("Falsos Positivos: "+this.fpn[1]+" Falsos Negativos: "+this.fpn[0]);
    }

    public void printMetricas() {
        // TODO Auto-generated method stub
        float ex = Formulas.exactitud(vpn[1], vpn[0], fpn[1], fpn[0]);
        float pr = Formulas.precision(vpn[1],fpn[1]);
        float exh = Formulas.exhaustividad(vpn[1],fpn[0]);
        float f1s = Formulas.f1_score(pr,exh);
        System.out.println("Exactitud: "+ex);
        System.out.println("Precision: "+pr);
        System.out.println("Exhaustividad: "+exh);
        System.out.println("F1_score: "+f1s);
    }
}

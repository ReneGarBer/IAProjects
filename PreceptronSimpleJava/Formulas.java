public class Formulas {

    public static float dot(float[]x,float[]w){
        float dot = 0;

        for(int i = 0; i < x.length-1; i++){
            dot += x[i]*w[i];
        }
        return dot;
    }

    public static float exactitud(int vp, int vn,int fp, int fn){
        return (float)(vp+vn)/(float)(vp+vn+fp+fn);
    }

    public static float precision(int vp, int fp){
        return (float)(vp)/(float)(vp+fp);
    }

    public static float exhaustividad(int vp, int fn){
        return (float)(vp)/(float)(vp+fn);
    }

    public static float f1_score(float pre, float exh){
        return 2*(pre*exh/(pre+exh));
    }
}

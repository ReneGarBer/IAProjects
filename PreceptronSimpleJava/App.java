public class App {
    public static void main(String[] args) throws Exception {
        //Creación del dataset
        DataSet dataset = new DataSet();
        String[] headers = {"x","y","z","label"};
        String path = "C:\\Users\\reneg\\OneDrive\\Desktop\\CUCEI\\SEMESTRE ULTIMO\\Seminario de Solución de Problemas de Inteligencia Artificial\\Documentos\\Practica 1\\spheres1d10.csv";
        dataset.setHeaders(headers);
        dataset.setDataFromCSV(path,3);
        dataset.print();

        //Creación del perceptron
        float l_rate = 0.05f;
        int epocas = 500;
        PerceptronSimple perceptronSimple = new PerceptronSimple(dataset,l_rate,epocas);

        //Pruebas utilizando distintas divisiones

        //Particion aleatoria
        dataset.divideDataSet(1);
        System.out.println("Metodo de particion: Aleatorio");
        System.out.println("Partición de entrenamiento");
        dataset.printTraining();

        System.out.println("Partición de prueba");
        dataset.printTest();

        perceptronSimple.entrenar(dataset.getTrainingtDataSet(),1.0f);

        perceptronSimple.probar(dataset.getTestDataSet());

        perceptronSimple.printmatriz();
        System.out.println();
        perceptronSimple.printMetricas();

        //Particion secuencial
        dataset.divideDataSet(2);
        System.out.println("Metodo de particion: Secuencial");
        System.out.println("Partición de entrenamiento");
        dataset.printTraining();

        System.out.println("Partición de prueba");
        dataset.printTest();

        perceptronSimple.entrenar(dataset.getTrainingtDataSet(),1.0f);

        perceptronSimple.probar(dataset.getTestDataSet());

        perceptronSimple.printmatriz();
        System.out.println();
        perceptronSimple.printMetricas();

        // //Particion Clasificador negativos
        dataset.divideDataSet(3);
        System.out.println("Metodo de particion: Clasificador negativos");
        System.out.println("Partición de entrenamiento");
        dataset.printTraining();

        System.out.println("Partición de prueba");
        dataset.printTest();

        perceptronSimple.entrenar(dataset.getTrainingtDataSet(),1.0f);

        perceptronSimple.probar(dataset.getTestDataSet());

        perceptronSimple.printmatriz();
        System.out.println();
        perceptronSimple.printMetricas();

        // //Particion Clasificador positivos
        dataset.divideDataSet(4);
        System.out.println("Metodo de particion: Clasificador positivos");
        System.out.println("Partición de entrenamiento");
        dataset.printTraining();

        System.out.println("Partición de prueba");
        dataset.printTest();

        perceptronSimple.entrenar(dataset.getTrainingtDataSet(),1.0f);

        perceptronSimple.probar(dataset.getTestDataSet());

        perceptronSimple.printmatriz();
        System.out.println();
        perceptronSimple.printMetricas();

        // //Particion Proporcional
        dataset.divideDataSet(5);
        System.out.println("Partición de entrenamiento");
        dataset.printTraining();

        System.out.println("Partición de prueba");
        dataset.printTest();

        perceptronSimple.entrenar(dataset.getTrainingtDataSet(),1.0f);

        perceptronSimple.probar(dataset.getTestDataSet());

        perceptronSimple.printmatriz();
        System.out.println();
        perceptronSimple.printMetricas();

    }
}

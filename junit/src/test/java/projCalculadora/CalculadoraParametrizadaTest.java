package projCalculadora;

import java.util.Arrays;
import java.util.Collection;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;
import static org.junit.Assert.*;

@RunWith(Parameterized.class)
public class CalculadoraParametrizadaTest {

    private int numero1;
    private int numero2;
    private int resultadoEsperado;

    public CalculadoraParametrizadaTest(int numero1, int numero2, int resultadoEsperado){
        this.numero1 = numero1;
        this.numero2 = numero2;
        this.resultadoEsperado = resultadoEsperado;
    }

    @Parameters(name = "{index}: Testando se {0} + {1} = {2}")
    public static Collection<Object[]> massaDeTestes(){
        return Arrays.asList(new Object[][]{
            {1, 1, 2},
            {2, 3, 99},
            {-1, 5, 4},
            {0, 0, 0,},
            {10, 20, 30}
        });
    }

    @Test
    public void deveriaSomarDoisNumerosCorretamente(){
        Calculadora calc = new Calculadora();
        System.out.println("Rodando teste: " + numero1 + " + " + numero2 + " = " + resultadoEsperado);
        assertEquals(resultadoEsperado, calc.soma(numero1, numero2));
    }

}
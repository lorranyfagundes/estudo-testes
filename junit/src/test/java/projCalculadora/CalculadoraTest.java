package projCalculadora;
import org.junit.Test;
import static org.junit.Assert.*;

import java.beans.Transient;

public class CalculadoraTest{
    @Test
    public void deveriaSomarDoisNumerosPositivos(){
        Calculadora calc = new Calculadora();
        assertEquals(2, calc.soma(1,1));
    }

    @Test
    public void deveriaSubtrairCorretamente(){
        Calculadora calc = new Calculadora();
        assertEquals(3,calc.subtracao(5,2));
    }

    @Test
    public void deveriaMultiplicarComPontoFlutuante(){
        Calculadora calc = new Calculadora();
        assertEquals(9, calc.multiplicacao(3,3), 0.1);
    }

    @Test
    public void deveriaDividirComPontoFlutuante(){
        Calculadora calc = new Calculadora();
        assertEquals(10, calc.divisao(20,2), 0.1);
    }

    @Test(expected = ArithmeticException.class) //o teste passa se esta exceção ocorrer
    public void deveriaLancarExcecaoAoDividirPorZero(){
        Calculadora calc = new Calculadora();
        calc.divisao(10, 0);
    }

    // testes de ehPositivo()
    @Test
    public void deveriaSerPositivoComNMaiorQueZero(){
        Calculadora calc = new Calculadora();
        //assertEquals(true, calc.ehPositivo(5));
        assertTrue(calc.ehPositivo(5));
    }
    
    @Test
    public void naoDeveSerPositivoComNMenorQueZero(){
        Calculadora calc = new Calculadora();
        assertEquals(false, calc.ehPositivo(-5));
    }

    @Test
    public void naoDeveSerPositivoComZero(){
        Calculadora calc = new Calculadora();
        assertEquals(false, calc.ehPositivo(0));
    }
}
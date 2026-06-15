package projCalculadora;
import java.util.Calendar;
import org.junit.Before;
import org.junit.Test;
import org.junit.After;
import static org.junit.Assert.*;

public class NegociacaoTest{
    
    private Calendar dataOriginal;

    @Before
    public void setUp(){
        //antes de cada teste, o junit cria uma data nova
        dataOriginal = Calendar.getInstance();
        dataOriginal.set(Calendar.DAY_OF_MONTH, 15);
    }

    @After
    public void tearDown(){
        //depois de cada teste limpa a var
        dataOriginal = null;
    }
    
    @Test(timeout = 5000) //falha se demorar mais de 1s
    public void dataDaNegociacaoDeveSerImutavel(){        
        Negociacao n = new Negociacao(dataOriginal);
        //Thread.sleep(500);
        // tenta mudar a data por fora
        dataOriginal.set(Calendar.DAY_OF_MONTH, 20);

        // vê se a data ainda é 15
        assertEquals(15, n.getData().get(Calendar.DAY_OF_MONTH));

    }
}
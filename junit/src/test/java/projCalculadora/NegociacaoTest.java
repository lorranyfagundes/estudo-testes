package projCalculadora;
import java.util.Calendar;
import org.junit.Test;
import static org.junit.Assert.*;

public class NegociacaoTest{
    @Test
    public void dataDaNegociacaoDeveSerImutavel(){
        Calendar dataOriginal = Calendar.getInstance();
        dataOriginal.set(Calendar.DAY_OF_MONTH, 15);
        
        Negociacao n = new Negociacao(dataOriginal);

        // tenta mudar a data por fora
        dataOriginal.set(Calendar.DAY_OF_MONTH, 20);

        // vê se a data ainda é 15
        assertEquals(15, n.getData().get(Calendar.DAY_OF_MONTH));

    }
}
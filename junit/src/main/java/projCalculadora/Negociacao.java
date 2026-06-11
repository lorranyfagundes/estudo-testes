package projCalculadora;
import java.util.Calendar;

public final class Negociacao{ // final impede herança que mude o comportamento
    private final Calendar data; // final no atributo impede reatribuição

    public Negociacao(Calendar data){
        this.data = (Calendar) data.clone();
    }

    public Calendar getData(){
        return (Calendar) this.data.clone();
    }
}
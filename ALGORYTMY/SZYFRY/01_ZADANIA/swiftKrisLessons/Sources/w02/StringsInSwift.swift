

class StringsInSwift {
    static func examples() {
        
        let text: String = "pretest" 
        
        let t: Character = "t" 
        //jednoliterowy String może być traktowany jako Character. Nie ma potrzeby konwersji.
        
        // Praca z typami String w Swift jest dość specyficzna żeby nie powiedzieć upierdliwa.
        // wynika to z faktu że String w Swift jest kolekcją znaków Unicode które mogą mieć różną długość w bajtach.
        // dlatego indeksy w Stringu nie są liczbami całkowitymi tylko specjalnym typem String.Index.
        // Jeśli nie chcemy martwić się o te szczegóły to możemy przekonwertować String na tablicę znaków Character.
        // Wtedy indeksy będą zwykłymi Intami. 

        let textA: [String.Element] = Array(text) 
        // String.Element to inaczej Character. to jest tak zwany type alias czyli inna nazwa tego samego typu.
        // public typealias Element = Character // tak to wygląda w dokumentacji String
        
        //wiele funkcji zwraca optionale (czyli wartość albo nic - nil). W typie oznaczamy to przez znak zapytania Po nazwie typu?
        let indexT1: String.Index?  = text.firstIndex(of: "t")
        let indexA1: Int?           = textA.firstIndex(of: t)
        
        //// takich typów nie można używać bezpośrednio bez rozpakowania (unwrapping).
        //// poniższy kod się nie skompiluje:
        //text.distance(from: text.startIndex, to: indexT4)
        //textA.distance(from: 0, to: indexA4)

        //za pomocą operatora ! można wymusić rozpakowanie. UWAGA: jeśli wartość jest nil to program się zawiesi (runtime error)
        //takie powiedzenie kompilatorowi: trust me Bro, I know what I'm doing!
        let indexT2: String.Index  = indexT1!
        let indexA2: Int            = indexA1!
        //lub wywołując firstIndex bezpośrednio z operatorem !:
        let indexT2b: String.Index  = text.firstIndex(of: t)!
        let indexA2b: Int            = textA.firstIndex(of: t)!
        
        //taki kod już się skompiluje (niemniej może się zawiesić w runtime jeśli nie znajdzie 't' w stringu)
        let distanceT1: Int  = text.distance(from: text.startIndex, to: indexT2)
        let distanceA1: Int  = textA.distance(from: 0, to: indexA2) //this is uselless?
        let distanceAB: Int = indexA2 - 0 //same as above in most cases!
        
        //wartości optional można też używać z znakiem zapytania ? aby bezpiecznie wywołać na nich funkcję. Taka funkcja zwróci nil jeśli indexA1 był nilem. 
        let sign: Int? = indexA1?.signum() 

        //można też użyć operatora ?? który pozwala podać wartość domyślną w przypadku nil
        //czyli w naszym przypadku jeśli nie znajdzie 't' w stringu to zwróci startIndex lub -1
        let indexT3: String.Index  = indexT1 ?? text.startIndex
        let indexA3: Int           = indexA1 ?? -1
        //lub wywołując firstIndex bezpośrednio z operatorem ??:
        let indexT3b: String.Index  = text.firstIndex(of: t) ?? text.startIndex
        let indexA3b: Int           = textA.firstIndex(of: t) ?? -1
        print("IndexA1 \(indexA1 ?? -1)")

        // w sumie możemy potraktować operator ?? jako skróconą instrukcję if ... else ...
        // zwróć uwagę że if ... else ... może być użyte jako wyrażenie zwracające wartość
        let indexT4: String.Index  = if (indexT1 != nil) { indexT1! } else { text.startIndex }
        let indexA4: Int           = if (indexA1 != nil) { indexA1! } else { -1 }
        
        //ale chyba najbezpieczniejszym sposobem jest użycie instrukcji if let która sprawdza czy wartość nie jest nil
        //i jeśli nie jest nil to nowa stała (u nas. indexT4) już nie ma typu optional tylko zwykły String.Index/Int
        if let indexT5: String.Index = text.firstIndex(of: t) { 
            //przykład użycia string-interpolacji do wyświetlenia wyniku. 
            // "text \(zmienna) text"
            print("found t1: \(text.distance(from: text.startIndex, to: indexT5)) index") 
        } 

        //ale chyba najbezpieczniejszym sposobem jest użycie instrukcji if let która sprawdza czy wartość nie jest nil
        //i jeśli nie jest nil to nowa stała (u nas. indexT4) już nie ma typu optional tylko zwykły String.Index/Int
        if let indexT5: String.Index = indexT1 { /** tu zrobić coś ze zmienną indexT5 */ } 
        
        //skrócony zapis gdzie indexT1 w bloku nagle nie ma typu optional tylko String.Index!
        // to ciekawe i prawdopodobnie polecane rozwiązanie
        if let indexT1: String.Index {
            print("found t1: \(text.distance(from: text.startIndex, to: indexT1)) index")
        } else {
            print("t not found")
        }

        ////poza zakresem if let nie można używać indexT4/indexA4 bo są zdefiniowane tylko w tym zakresie
        /// poniższy kod się nie skompiluje:
        //print("found t: \(text.distance(from: text.startIndex, to: indexT4))")

        ///multi-line string literal. Wymaga entera po trzech cudzysłowach na początku i na końcu!
        print("""
            end of program
            end of dreams
            """)
    }
}

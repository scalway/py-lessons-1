// 2. Gaderypoluki – Szyfr z słowem kluczem

// Ten szyfr polega na tym, że bierzemy jakieś długie słowo składające się z niepowtarzających się liter oraz sylab dwuliterowych i zamieniamy szyfrowaną literę na tą drugą z sylaby naszego słowa klucza, a te litery, które nie występują w szyfrowanym haśle przepisujemy bez zmian.

// Inne przykładowe słowa klucze:
// MA-LI-NO-WE-BU-TY
// PO-LI-TY-KA-RE-NU
// BI-TW-AO-CH-MU-RY


// przyklad 

// Klucz: GA-DE-RY-PO-LU-KI
// Tekst do szyfrowania: JESTEŚMY NA WCZASACH
// Tekst zaszyfrowany:
// JDSTDSMR NG WCZGSGCH

//key needs to be upercased

func gaderyKuba(_ text:String, key: String = "GA-DE-RY-PO-LU-KI") -> String {
    var arrayKey = Array(key).split(separator: "-")
    var result = ""

    for i: Character in text.uppercased() {
        var pair = arrayKey.first(where: { $0.contains(i) })

        if let pair {
            let si: Int = pair.startIndex
            if (pair[si] == i) {
                result.append(pair[si + 1])
            } else {
                result.append(pair[si])
            }
        } else {
            result.append(i)
        }
    }

    return result
}

func gaderyKris(_ text:String, key: String = "GA-DE-RY-PO-LU-KI") -> String {
    var arrayKey = Array(key.uppercased())

    var result = ""
    var textUp = text.uppercased()

    for idx: String.Index in textUp.indices {
        let i = text[idx]
        let iu = textUp[idx]
        let index: Int? = arrayKey.firstIndex(where: { s in s == iu })
        let encoded: Character = if let index: Int {
            switch index % 3 {
            case 0: arrayKey[index + 1]
            case 1: arrayKey[index - 1]
            default: i //for "-" sign
            } 
        } else { i }
        
        if (i.isUppercase) { 
            result.append(encoded) 
        } else { 
            result.append(i.lowercased())       //było
            result.append(encoded.lowercased()) //powinno być
        }
    }

    return result
}

func exampleGadery(){
    func run(_ text: String){
        print("wywolano gadery dla tekstu \(text):\(gaderyKris(text))")
    }
    run("abA")
    run("ark")
    run("ak a")
}
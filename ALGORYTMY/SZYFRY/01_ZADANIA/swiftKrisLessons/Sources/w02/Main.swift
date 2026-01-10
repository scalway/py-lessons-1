// The Swift Programming Language
// https://docs.swift.org/swift-book
// 
// author: Krzysztof Pecyna
//
// program utworzony w vs-code przez:
// ctrl+shift+p -> Swift Create New Project -> Executable -> nazwa projektu: w02
// istotne głównie dlatego że tworzy plik Package.swift i strukturę katalogów. 
// bez pliku Package.swift vscode nie podpowiada składni ani nie pokazuje dokumentacji dla języka i biblioteki Swift
//
// Domyślnie vscode wywoła komendy swift package za nas ale może się zdarzyć że zmienimy Package.swift 
// i trzeba będzie ręcznie wywołać aby pobrać zależności i zaktualizować pliki konfiguracyjne projektu:
// ```swift package clean; swift package resolve; swift package update```
// 

@main
struct Main {
    static func main() {
        StringsInSwift.examples()
    }
}

// koniecznie zajrzyj na stronę:
// https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour/
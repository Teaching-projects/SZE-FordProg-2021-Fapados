# SZE-FordProg-2021-Fapados
Tozser Zoltan

Leírás: 

A tests mappában fájlok vannak, amelyek valid vagy invalid JSON fájlok. A test.py fájlt futtatva a program kiértékeli a JSON fájlokat, tehát eldönti, hogy valid vagy invalid és egy összegző fájlt készít (tests_results néven) a tests mappába. 

Három fájlból áll a program:lex, parse és a test. 

Az összes érvényes token JSON formátumban történő meghatározását a JSONLlexer osztály adja meg a JSON_lex.py-ben.

A JSONLexer osztály tartalmazza az összes szükséges reguláris kifejezést (RegEx) a minta JSON bemenet osztályjellemzőkként történő megfelelő tokenizálásához. 

A tokenek regexei közül néhány osztály attribútumként van definiálva, de maguk a tokenek definíciói osztály metódusként vannak feltüntetve.

A hibakeresés megkönnyítése érdekében minden alkalommal, amikor új sor karaktert találunk, a lexer.lineno változó növekszik. 

Amikor bal kapcsoszárójelet vagy szögleteszárójelet észlel, a megfelelő adatszerkezet mélységét a JSONLexer osztályban tárolja.

Ha nem definiált tokent észlel, akkor hiba lép fel és az elemzés leáll (SyntaxError("Illegal character...)).

A build metódus felelős a lexer felépítéséért.

A JSONLexer osztályt a JSONParser osztályból hívják meg. 

Ennek az osztálynak az a szerepe, hogy megbizonyosodjon arról, hogy a lexertől kapott jelzőknek megfelelő-e a szintaxisuk és a nyelvtanuk. 

Elemzi a bemenetet és a kimentetre a log fájlba írja az eredményeket. 

A JSONParser init függvényben lexer-példányt hívunk meg és a lexer felépül. 

A JSONParser.p_error függvény szintaktikai hibát vizsgál és ha ilyet észlel, akkor leállítja az elemzést.

A JSON fájlok parsolásakor néhány hiba esetet itt megnevesítenék:

Az 1. JSON fájl parsolásakor hiányzik a záró kapcsoszárójel, ezért szintaktikai hibaként megjelenik a log fájlban a "You seem to have an unclosed object." hibaüzenet, ezért lesz invalid a fájl. 

A 4. JSON fájlnál a harmadik idézőjel nem kell bele, ezért szintaktikai hibát küld (SyntaxError("Illegal character..."). 

Az 5. JSON fájl parsolásakor hiányzik egy záró szögletes zárójel a kapcsoszárójel előtt, ezért szintaktikai hibaként megjelenik a log fájlban a SyntaxError("Error on line ...). 

A 6. JSON fájlban mindösszessen egy entert tartalmaz, ezért parzoláskor az alábbi szintaktikai hiba generálódik a results.log fájlban: ("There's something wrong...")

A program elkészíti a parsetab.py (LALR) fájlt és a parser.out-ot is. 

Az eredmény fájlban látható, hogy vannak valid és nem valid eredmények is. 

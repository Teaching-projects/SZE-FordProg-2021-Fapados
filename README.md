# SZE-FordProg-2021-Fapados
Tozser Zoltan

Leírás: 

A tests mappában fájlok vannak, amelyek valid vagy invalid JSON fájlok. A program kiértékeli őket, tehát eldönti, hogy valid vagy invalid és egy összegző fájlt készít (tests_results néven) a tests mappába. 

Három fájlból áll a program:lex, parse és a test. 

Az összes érvényes token JSON formátumban történő meghatározását a JSONLlexer osztály adja meg a JSON_lex.py-ben.

A JSONLexer osztály tartalmazza az összes szükséges reguláris kifejezést (RegEx) a minta JSON bemenet osztályjellemzőkként történő megfelelő tokenizálásához. 

A tokenek regexei közül néhány osztály attribútumként van definiálva, de maguk a tokenek definíciói osztály metódusként vannak feltüntetve.

A hibakeresés megkönnyítése érdekében minden alkalommal, amikor új sor karaktert találunk, a lexer.lineno változó növekszik. 

Amikor bal kapcsoszárójelet vagy szögleteszárójelet észlel, a megfelelő adatszerkezet mélységét a JSONLexer osztályban tárolja.

Ha nem definiált tokent észlel, akkor hiba lép fel és az elemzés leáll.

A build metódus felelős a lexer felépítéséért.

A JSONLexer osztályt a JSONParser osztályból hívják meg. 

Ennek az osztálynak az a szerepe, hogy megbizonyosodjon arról, hogy a lexertől kapott jelzőknek megfelelő-e a szintaxisuk és a nyelvtanuk. 

A JSONParser init függvényben lexer-példányt hívunk meg és a lexer felépül. 

A JSONParser.p_error függvény szintaktikai hibát vizsgál és ha ilyet észlel, akkor leállítja az elemzést.

A program elkészíti a parsetab.py fájlt és a parser.out-ot is. 

Az eredmény fájlban vannak valid és nem valid eredmények. 
